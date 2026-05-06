import joblib
import os

model = joblib.load(os.path.join("ml", "model.pkl"))

def predict(features):
    return model.predict([features])[0]