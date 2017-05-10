import requests
import json

json_body = requests.get('https://api.coinmarketcap.com/v1/ticker/monero').text
body = json.loads(json_body)

f=open('moneroprice.csv','a')
f.write('\n')
f.write(body[0]['price_usd'])
f.close()
