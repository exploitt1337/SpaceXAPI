from spacex.spacex import SpaceXAPI
from flask import Flask, request, jsonify

port = 1010
class SellixWebhook:
    def __init__(self):
        self.spacex = SpaceXAPI()

    def process_order(self, payload):
        order_id = payload.get('order_id')
        return

    def generate_key(self, request_type, amount):
        response = self.spacex.generate(request_type, amount)
        return response

app = Flask(__name__)
webhook = SellixWebhook()

@app.route('/offline', methods=['POST'])
def generate_offline():
    data = request.get_json()['data']
    response = webhook.generate_key('offline', data['quantity'])
    key, url = response['key'], response['url']
    return str({"key": key, "url": url})

@app.route('/online', methods=['POST'])
def generate_online():
    data = request.get_json()['data']
    response = webhook.generate_key('online', data['quantity'])
    key, url = response['key'], response['url']
    return str({"key": key, "url": url})

def run():
    app.run(host="0.0.0.0", port=port)
