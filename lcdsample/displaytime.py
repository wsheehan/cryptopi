# This python script should display the current time over five ten second intervals then turn off

# Initializations
import time
import Adafruit_CharLCD as LCD
from datetime import datetime

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

# Wipe whatever was previously on the screen and load our message
lcd.clear()
lcd.message('Hit select!')

# Initialize counter
counter = 0

while counter < 3:
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(datetime.now().strftime('%H:%M:%S'))
        time.sleep(1.0)
        counter+=1

lcd.clear()        
lcd.message('Give new py file...')    


