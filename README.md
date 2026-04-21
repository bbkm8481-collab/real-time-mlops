# 🚀 Real-Time Fraud Detection & Streaming MLOps Pipeline

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-Streaming-black.svg?logo=apachekafka)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg?logo=docker)](https://www.docker.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C.svg?logo=prometheus)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800.svg?logo=grafana)](https://grafana.com/)

## 📖 Project Overview
This repository contains a full-scale, event-driven MLOps architecture designed to ingest, process, and evaluate streaming transaction data in real-time. It demonstrates the ability to transition static machine learning models into high-throughput, distributed microservices.

## 🏗️ Enterprise Architecture
This system simulates a real-world financial security pipeline, utilizing a containerized microservices architecture:
1. **API Gateway (FastAPI):** Acts as the Point of Sale (POS) entry point, receiving credit card swipes and pushing them to a message broker.
2. **Message Broker (Apache Kafka & Zookeeper):** Handles high-volume, real-time event streaming and guarantees message delivery.
3. **AI Inference Worker (Python/Scikit-Learn):** A background consumer that instantly catches Kafka events, runs them through a serialized ML model, and flags fraudulent transactions in milliseconds.
4. **Observability Stack (Prometheus & Grafana):** Actively monitors API health, system throughput, and inference latency.

## 🛠️ Tech Stack
* **Streaming Engine:** Apache Kafka, Zookeeper, `confluent-kafka`
* **Microservices:** FastAPI, Uvicorn, Docker, Docker Compose
* **Machine Learning:** Scikit-Learn, Pandas, Joblib (Logistic Regression Baseline)
* **Observability:** Prometheus, Grafana, `prometheus-fastapi-instrumentator`

## 📊 Live Telemetry & Load Testing
The system is heavily instrumented to provide real-time observability into the streaming pipeline. Below is a simulated load test capturing a burst of API traffic successfully routed through the Kafka broker.

*(Drag and drop your grafana-spike.png image here!)*

## 🚀 How to Run the Cluster Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/bbkm8481-collab/real-time-mlops.git](https://github.com/bbkm8481-collab/real-time-mlops.git)
cd real-time-mlops
```

**2. Launch the Cloud Infrastructure:**
```bash
docker-compose up --build -d
```

**3. Access the Control Centers:**
* **Trigger a Transaction (Swagger UI):** `http://localhost:8000/docs`
* **View the Live Dashboard (Grafana):** `http://localhost:3000`
* **Watch the AI Logs:** `docker logs -f fraud-consumer`
```

<img width="784" height="517" alt="Screenshot 2026-04-21 at 11 15 03 PM" src="https://github.com/user-attachments/assets/e2f99b42-af4d-4d0b-8cfb-161193f02396" />
