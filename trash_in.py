import os
from uuid import uuid4
import dotenv
from datetime import datetime, timedelta
import json
import requests

dotenv.load_dotenv()

def send_message(message):
    url = os.getenv("WHATSAPP_URL")
    number = os.getenv("NUMBER")
    payload = json.dumps({"chatId": f"{number}@g.us", "message": message})
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=payload)
    print("response", response.text.encode("utf8"))

if __name__ == "__main__":
    message = (
        "THE FOLLOWING MESSAGE IS SENT VIA A BOT:\n\n"
        "🗑️ Reminder: Please bring the trash in from 1152 Street curb at 1152 this morning (Tuesday)! 🗑️\n\n"
        "Let's keep our place clean and tidy. Thank you! 😊"
    )
    send_message(message)