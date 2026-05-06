import numpy as np
from .ml_model import predict

def build_features(prices):
    if len(prices) < 6:
        return None
    return np.diff(prices[-6:-1])

def get_signal(prices):
    features = build_features(prices)
    if not features is None:
        result = predict(features)
        return "BUY" if result == 1 else "SELL"
    return None