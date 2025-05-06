from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "XAUUSD Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)
    return 'Webhook received!', 200
