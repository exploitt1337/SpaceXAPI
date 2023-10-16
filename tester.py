import requests 
r = requests.post("http://127.0.0.1:1010/offline", json={"data":{"amount": 1}})
print(r.json())