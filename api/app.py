from fastapi import FastAPI
import pandas as pd
import json
import random
from confluent_kafka import Producer
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Real-Time Fraud API Gateway")

# Connect to Kafka
producer_config = {'bootstrap.servers': 'kafka:29092'} # Updated to use Docker network name!
producer = Producer(producer_config)
topic_name = 'live_transactions'

print("Loading data for API simulation...")
df = pd.read_csv('data/fraud.csv')
fraud_txns = df[df['Class'] == 1]
normal_txns = df[df['Class'] == 0]

@app.post("/swipe/{txn_type}")
async def simulate_swipe(txn_type: str):
    if txn_type.lower() == "fraud":
        row = fraud_txns.sample(1).iloc[0]
    else:
        row = normal_txns.sample(1).iloc[0]

    features = row.drop(['Class', 'Time']).to_dict()
    txn_id = f"API-TXN-{random.randint(10000, 99999)}"

    payload = {
        "transaction_id": txn_id,
        "features": features,
        "true_label": int(row['Class'])
    }

    producer.produce(topic_name, value=json.dumps(payload))
    producer.flush()

    return {"status": "success", "transaction_id": txn_id, "injected_type": txn_type.upper()}

# 🚀 NEW: Start the Prometheus Instrumentator to track API metrics
Instrumentator().instrument(app).expose(app)
