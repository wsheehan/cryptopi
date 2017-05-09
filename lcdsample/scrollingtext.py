'''
import requests
import json

json_body = requests.get('http://www.coinwarz.com/v1/api/coininformation/?apikey=da1dc6513d1a45ef8a64c7bd733452d6&cointag=XMR').text
body = json.loads(json_body)

print(body['Data'])
'''
import math
import time

import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs        = 27  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                                      lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()
message = 'Scroll'
lcd.message(message)
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()
