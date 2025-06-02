import requests
import os

# Ortam değişkenleri
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

# Yapay zeka mesajı üret
def generate_message():
    prompt = (
        "Bir yazılımcının gözünden, sabah Slack kanalında paylaşılacak espirili, Türkçe, kısa ve yaratıcı bir günaydın mesajı yaz. Kod, bug, kahve, vs. içerebilir."
    )
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://github.com",  # İstersen GitHub linkini gir
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "mistralai/mixtral-8x7b",  # Daha stabil, önerilen model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)

    print(response.json())  # ✅ Bu satır şimdi doğru girintili

    return response.json()['choices'][0]['message']['content'].strip()

# Slack'e mesaj gönder
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
