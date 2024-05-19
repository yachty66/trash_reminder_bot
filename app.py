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
        "🗑️ Reminder: Please take out the trash today (Thursday)! 🗑️\n\n"
        "Please move the trash bins from the back of the house to the street curb at 1152. Let's keep our place clean and tidy. Thank you! 😊"
    )
    send_message(message)