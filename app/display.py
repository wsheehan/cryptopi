import time
import requests

# Import Adafruit lib
import Adafruit_CharLCD as LCD

# Initialize screen
lcd = LCD.Adafruit_CharLCDPlate()
lcd.clear()

# Pool API endpoint
API_URL = "http://127.0.0.1:8117"

running = True

while running
	if lcd.is_pressed(LCD.SELECT)
		lcd.message('powering down')
		return
	data = requests.get(API_URL)
	lcd.message(data) # Obviously would become more nuanced
	time.sleep(30)