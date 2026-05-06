import random
from bot.services.bot_runner import BotRunner

bot = BotRunner()

for _ in range(100):
    price = random.uniform(100, 200)
    bot.on_price(price)