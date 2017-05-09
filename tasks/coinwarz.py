import requests
import json

json_body = requests.get('http://www.coinwarz.com/v1/api/coininformation/?apikey=da1dc6513d1a45ef8a64c7bd733452d6&cointag=XMR').text
body = json.loads(json_body)

print(body['Data'])
