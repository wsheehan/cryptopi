import requests
import json

json_body = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin').text
body = json.loads(json_body)

print(body[0]['id'])
