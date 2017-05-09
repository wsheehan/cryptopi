import Adafruit_CharLCD as LCD
from subprocess import *
from datetime import datetime
import requests
import json
from time import sleep
import math

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize counter
counter = 0

json_body = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin').text
body = json.loads(json_body)
json_body1 = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum').text
body1 = json.loads(json_body1)

# Wipe whatever was previously on the screen and load our message
lcd.clear()
message = 'Select:XMR\nRight:ETH'
lcd.message(message)
while counter == 0:
    for i in range(len(message)):
        sleep(0.5)
        lcd.move_left()
        if lcd.is_pressed(LCD.SELECT):
            lcd.clear()
            counter+=1    
        if lcd.is_pressed(LCD.RIGHT):
            lcd.clear()
            counter+=1

while counter < 5:
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message('BTC USD:') 
        lcd.message(body[0]['price_usd'])
        sleep(1.0)
        counter+=1
    if lcd.is_pressed(LCD.RIGHT):
        lcd.clear()
        lcd.message('ETH USD:')
        lcd.message(body1[0]['price_usd'])
        sleep(1.0)
        counter+=1
        
lcd.clear()
lcd.message('Give new py file...')
