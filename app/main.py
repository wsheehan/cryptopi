import requests
import json

# Our current coins of interest
coins = {
	'monero': None,
	'ethereum': None,
	'litecoin': None
}

# Fetch coin data
uri = 'https://api.coinmarketcap.com/v1/ticker/'
def get_coin_data(coin):
	j = requests.get(uri + coin).text
	return json.loads(j)[0]

# Update coin data from api
for k, v in coins.items():
	coins[k] = get_coin_data(k)

print(coins)
