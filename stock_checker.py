import time
import requests
from bs4 import BeautifulSoup
import random

URL = "https://www.ktown4u.com/iteminfo?grp_no=3190592&goods_no=158911"

BOT_TOKEN = "你的BOT_TOKEN"
CHAT_ID = "你的CHAT_ID"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def check_stock():
    try:
        resp = requests.get(URL, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text(" ", strip=True)

        if "Out Of Stock" in text:
            return False
        else:
            return True

    except Exception as e:
        print("error:", e)
        return None

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

last_status = False

while True:
    status = check_stock()

    if status and not last_status:
        send_telegram(f"🔥 補貨了！快買：{URL}")

    last_status = status

    time.sleep(random.randint(120, 300))
