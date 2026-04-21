import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

print("1. Loading dataset (this might take a few seconds)...")
df = pd.read_csv('data/fraud.csv')

print("2. Preparing data...")
X = df.drop(columns=['Class', 'Time'])
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("3. Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("4. Evaluating model...")
score = model.score(X_test, y_test)
print(f"Baseline Accuracy: {score * 100:.2f}%")

print("5. Saving model...")
joblib.dump(model, 'model/model.pkl')
print("Training complete! Model saved to model/model.pkl")
