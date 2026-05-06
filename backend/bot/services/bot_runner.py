import time
import random
from .strategy import get_signal

BASE = 1
STEP = 0.5
MAX_RECOVERY = 5
MAX_STAKE = 7

class BotRunner:
    def __init__(self):
        self.prices = []
        self.recovery = 0
        self.stake = BASE

    def on_price(self, price):
        self.prices.append(price)

        if len(self.prices) > 50:
            self.prices.pop(0)

        signal = get_signal(self.prices)

        if not signal:
            return

        result = self.execute(signal)

        if result == "WIN":
            self.recovery = 0
            self.stake = BASE
        else:
            self.recovery += 1
            if self.recovery > MAX_RECOVERY:
                print("STOP BOT")
                return
            self.stake = min(BASE + STEP * self.recovery, MAX_STAKE)

        time.sleep(2)

    def execute(self, signal):
        print(f"{signal} | stake: {self.stake}")
        return random.choice(["WIN", "LOSS"])