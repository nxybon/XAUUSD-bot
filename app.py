from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram config
BOT_TOKEN = '7594556310:AAFD54kOSyomxaH9x7YEEDqy45uCqWZHcQ4'
CHAT_ID = '1989190767'  # or '@yourchannel'

@app.route('/')
def home():
    return "XAUUSD Bot is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"XAUUSD SIGNAL:\n{data.get('message', str(data))}"
    send_to_telegram(message)
    return 'Sent to Telegram!', 200

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'HTML'}
    requests.post(url, data=payload)
