from confluent_kafka import Consumer
import json
import joblib
import pandas as pd
import warnings

# Suppress sklearn warnings for cleaner output
warnings.filterwarnings('ignore')

print("1. Loading ML Model into memory...")
# We load the brain we trained in Phase 1
model = joblib.load('model/model.pkl')

print("2. Connecting to Kafka Broker...")
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'fraud-detection-group',
    'auto.offset.reset': 'earliest' # Start reading from the oldest unread message
}
consumer = Consumer(consumer_config)

topic_name = 'live_transactions'
consumer.subscribe([topic_name])

print(f"3. 🎧 Listening for live transactions on topic: '{topic_name}'...")
print("=" * 60)

try:
    while True:
        # Poll Kafka for a new message every 1 second
        msg = consumer.poll(1.0)

        if msg is None:
            continue # No new message, keep listening
        if msg.error():
            print(f"❌ Kafka Error: {msg.error()}")
            continue

        # 1. Catch the message and decode the JSON
        raw_data = msg.value().decode('utf-8')
        transaction = json.loads(raw_data)
        
        txn_id = transaction['transaction_id']
        features = transaction['features']
        true_label = transaction['true_label'] # We just use this to verify if our model is right!
        
        # 2. Format data for the ML model
        df_features = pd.DataFrame([features])
        
        # 3. REAL-TIME INFERENCE!
        prediction = model.predict(df_features)[0]
        
        # 4. Display the results beautifully
        if prediction == 1:
            print(f"🚨 FRAUD BLOCKED!  | ID: {txn_id} | Actual: {true_label}")
        else:
            print(f"✅ TXN APPROVED    | ID: {txn_id} | Actual: {true_label}")

except KeyboardInterrupt:
    print("\n🛑 Shutting down Consumer...")
finally:
    consumer.close()
