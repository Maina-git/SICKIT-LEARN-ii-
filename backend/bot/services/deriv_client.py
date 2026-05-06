import websocket
import json
import os
from dotenv import load_dotenv
from .bot_runner import BotRunner

load_dotenv()

TOKEN = os.getenv("DERIV_API_TOKEN")

bot = BotRunner()

def on_message(ws, message):
    data = json.loads(message)

    if "tick" in data:
        price = data["tick"]["quote"]
        bot.on_price(price)

def on_open(ws):
    ws.send(json.dumps({"authorize": TOKEN}))
    ws.send(json.dumps({"ticks": "R_100", "subscribe": 1}))

def run():
    ws = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3?app_id=1089",
        on_open=on_open,
        on_message=on_message
    )
    ws.run_forever()