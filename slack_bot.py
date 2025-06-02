import requests
import openai
import os

# API anahtarları
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY

def generate_message():
    prompt = (
        "Türkçe, yazılımcı bakış açısıyla, Slack kanalında paylaşılacak espirili, kısa ve yaratıcı bir günaydın mesajı yaz. "
        "Kod, bug, commit, kahve gibi terimlere göndermeler olabilir. 1-2 cümle yeterlidir."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ✅ en ucuz model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.9
    )

    return response.choices[0].message["content"].strip()

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
    message = generate_message()
    send_message_to_slack(message)

if __name__ == "__main__":
    main()
