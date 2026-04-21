import pandas as pd
import joblib

print("1. Loading saved model...")
model = joblib.load('model/model.pkl')

print("2. Grabbing a test transaction from the dataset...")
df = pd.read_csv('data/fraud.csv', nrows=5)

test_transaction = df.drop(columns=['Class', 'Time']).iloc[[0]]

print("3. Running inference...")
prediction = model.predict(test_transaction)

print("-" * 30)
if prediction[0] == 0:
    print("Prediction: NORMAL Transaction (0)")
else:
    print("Prediction: FRAUDULENT Transaction (1)")
print("-" * 30)
