import pandas as pd
from confluent_kafka import Producer
import json
import time

print("1. Connecting to Kafka Broker...")
producer_config = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_config)

# The "mailbox" we are sending data to
topic_name = 'live_transactions'

# Callback function to confirm delivery
def delivery_report(err, msg):
    if err is not None:
        print(f" Delivery failed: {err}")
    else:
        print(f" Sent Transaction to Kafka -> Topic: {msg.topic()}")

print("2. Loading dataset for simulation...")
df = pd.read_csv('data/fraud.csv')

print("3. Starting real-time stream simulation (Press Ctrl+C to stop)...")
print("-" * 50)

# Loop through the dataset row by row
for index, row in df.iterrows():
    # In the real world, the bank doesn't know if it's fraud yet!
    # So we separate the features from the true label.
    features = row.drop(['Class', 'Time']).to_dict()
    
    transaction_payload = {
        "transaction_id": f"TXN-{index + 1000}",
        "features": features,
        "true_label": int(row['Class']) # We keep this secretly to evaluate our model later
    }
    
    # Convert dictionary to JSON string
    json_data = json.dumps(transaction_payload)
    
    # Shoot the data into Kafka
    producer.produce(topic_name, value=json_data, callback=delivery_report)
    producer.poll(0) # Trigger the delivery report
    
    # Pause for 0.5 seconds to simulate real-time traffic
    time.sleep(0.5)

producer.flush()
