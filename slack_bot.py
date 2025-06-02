import requests
import openai
import os

# Ortam değişkenleri
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# OpenAI API yapılandırması
openai.api_key = OPENAI_API_KEY

# Yapay zeka mesajı üret
def generate_message():
    prompt = (
        "Bir yazılımcının gözünden, sabah Slack kanalında paylaşılacak espirili, Türkçe, kısa ve yaratıcı bir günaydın mesajı yaz. "
        "Kod, bug, commit, kahve gibi konulara gönderme yapılabilir. Samimi, doğal ve hafif mizahi olsun."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # gpt-4o varsa, yoksa "gpt-4" da olur
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.9
    )

    return response.choices[0].message["content"].strip()

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
