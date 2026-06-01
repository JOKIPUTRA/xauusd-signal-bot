import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OANDA_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_xau_price():
    url = "https://api-fxpractice.oanda.com/v3/accounts"

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        return None

    accounts = r.json()["accounts"]

    if not accounts:
        return None

    account_id = accounts[0]["id"]

    url = (
        f"https://api-fxpractice.oanda.com/v3/accounts/"
        f"{account_id}/pricing?instruments=XAU_USD"
    )

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        return None

    data = r.json()

    if not data["prices"]:
        return None

    bid = float(data["prices"][0]["bids"][0]["price"])
    ask = float(data["prices"][0]["asks"][0]["price"])

    return {
        "bid": bid,
        "ask": ask
    }
