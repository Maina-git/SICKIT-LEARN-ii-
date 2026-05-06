import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

X, y = [], []

for _ in range(2000):
    prices = np.random.rand(6)
    features = np.diff(prices[:-1])
    X.append(features)
    y.append(1 if prices[-1] > prices[-2] else 0)

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")
print("Model saved")