import requests
import os
import json
import random

# API anahtarları
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]

# JSON dosyasının yolu
JOKES_JSON_PATH = "gunaydin_esprileri.json"

def load_jokes_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("jokes", [])

def select_random_joke(jokes):
    return random.choice(jokes)

def send_message_to_slack(text):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "channel": SLACK_CHANNEL_ID,
        "text": text
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())

def main():
    try:
        jokes = load_jokes_from_file(JOKES_JSON_PATH)
        if not jokes:
            raise ValueError("JSON içinde espri bulunamadı.")
        message = select_random_joke(jokes)
        send_message_to_slack(message)
    except Exception as e:
        print("Hata oluştu:", str(e))

if __name__ == "__main__":
    main()
