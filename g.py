from spacex.spacex import SpaceXAPI 

spacex = SpaceXAPI()

request_type = input("Enter type (offline/online): ")
amount = float(input("Enter amount: "))
response = spacex.generate(request_type, amount)

if not response.get('error'):
    key, url = response['key'], response['url']
    print(f'Key: {key}\nURL: {url}')
else:
    print(f'Error: {response["message"]}')

