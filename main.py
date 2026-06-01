import schedule
import time

from oanda_client import get_xau_price
from telegram_bot import send_message

def check_market():

    price = get_xau_price()

    if not price:
        return

    msg = f"""
XAUUSD LIVE

Bid : {price['bid']}
Ask : {price['ask']}
"""

    send_message(msg)

schedule.every(1).minutes.do(check_market)

send_message("Bot XAUUSD berhasil dijalankan")

while True:
    schedule.run_pending()
    time.sleep(1)
