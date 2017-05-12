import requests
import json
import math

# Pulling the data from CoinWarz
json_body0 = requests.get('http://www.coinwarz.com/v1/api/profitability/?apikey=8908d5494a13471ba21317b5fe01a088&algo=all').text
body0 = json.loads(json_body0)

x = body0['Data']

coins = {"Monero": None, "Litecoin": None, "Ethereum": None}

def set_coin_data(line):
    for coin in coins.iteritems():
        print(coin)
        if line['CoinName']==coin:
            print("Firing")
            coins[coin] = line

for line in x:
        set_coin_data(line)

print(coins)

