import requests
import json
from flask import Flask, request

app = Flask(__name__)

# WhatsApp API credentials
WHATSAPP_API_URL = "https://graph.facebook.com/v17.0/672790196767618/messages"
ACCESS_TOKEN = "EAAJNB9sCpu8BO3WX1Rtsr9t4FRes6wLt0HN41Wx27HtZBPchbevaXJWwonwK3WfRNHZBfmQjpVaWoiNpCHCq5cboeE1O31Ol38tGkWwD3QF2iRtpxDx8tivW432Te2jhGfBYxUkjcG242gGuBDmCwD4ubFEXHzeMExUi6lCxbHS1Fa3NT5vVFJtZAUnwIZCwifArLAnmLRxZCx0ZCXZCMQkPaZCpuV0KwxAiuR7HDM6g0q4ZD"

@app.route('/webhook', methods=['POST'])
def order_webhook():
    data = request.json
    customer_name = data['customer']['first_name']
    customer_phone = data['customer']['phone']
    order_id = data['id']

    # Prepare WhatsApp message
    message = {
        "messaging_product": "whatsapp",
        "to": customer_phone,
        "type": "template",
        "template": {
            "name": "order_confirmation",
            "language": {"code": "en_US"},
            "components": [{
                "type": "body",
                "parameters": [{"type": "text", "text": customer_name}, {"type": "text", "text": order_id}]
            }]
        }
    }

    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    response = requests.post(WHATSAPP_API_URL, headers=headers, json=message)

    return {"status": "Message sent!"}, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
