import requests

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot7594556310:AAFD54kOSyomxaH9x7YEEDqy45uCqWZHcQ4/sendMessage"
    payload = {
        "chat_id": "1989190767",  # Use your channel ID if posting to a group/channel
        "text": message
    }
    requests.post(url, json=payload)
