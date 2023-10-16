import requests
import json

class SpaceXAPI:
    def __init__(self):
        with open('config.json', 'r') as file:
            data = json.load(file)
            self.base_url = data.get('base_url')
            self.license = data.get('license')

    def generate(self, request_type, amount):
        url = f'{self.base_url}/generate'
        payload = {'type': request_type, 'license': self.license, 'amount': amount}
        response = requests.post(url, json=payload)
        return response.json()
    
    def balance(self):
        url = f'{self.base_url}/balance'
        payload = {'license': self.license}
        response = requests.get(url, params=payload)
        return response.json()

if __name__ == '__main__':
    spacex = SpaceXAPI()
    request_type = input("Enter type (offline/online): ")
    amount = int(input("Enter amount: "))
    response = spacex.generate(request_type, amount)
    
    if not response.get('error'):
        key, url = response['key'], response['url']
        print(f'Key: {key}\nURL: {url}')
    else:
        print(f'Error: {response["message"]}')
