# Craig's Daily Notes

# Wednesday April 26, 2017

* kai told us about github pages
* Completed cron datetime task
  * Used crontab -e to edit system cron jobs
  * Needed new line at end of file to run
* Determined cryptocurrencies to mine with our pi
  * Want to avoid SHA-256 proof of work algorithms
  * Litecoin uses scypt algorithm and is seemingly profitable
  * Ethereum has a lot of potential as a currency and is profitable/not on SHA-256
  * Monero, uses algorithm suitable for personal computers and has promise
  * All three are quite stable at this point sitting at 4th, 2nd, and 6th in market caps
* Learned basic Git commands 
  * learned how to clone directory 
  * practices pulling, adding, commiting, and pushing

# Thursday April 27, 2017

* Email Task
  * use socket to retrieve IP address
  * use pythons smtp server to send mail
  * new email is cryptoraspberrypi@gmail.com
  * send on boot from `/etc/rc.local`
  * Final file in `tasks/ip_address_email.py`
* Configuring MINGW64 on Desktop
  * generated ssh key and added to github
  * realized to had to run MINGW64 as administrator to use git clone
  * raelized didn't have emacs, had to use this vi editor 
  * edited this post from desktop computer
* Project planning
  * schematic of services
  * checked docker images of each coin
  * lcd display may force us to use python and not node.js or ruby 

# Monday May 1, 2017

* Initial Raspberry Pi Setup 
  * Installed heatsinks onto Raspberry Pi 
  * Used clearpass to register our device 
  * Successfully SSH'd into our Pi and installed emacs and Git 
  * Copied over py file to email us the IP address upon booting up 

* LCD Display 
  * Found online manual to connect LCD display parts 
  * Verified all parts were account for

# Tuesday May 2, 2017

* Building the LCD Display 
  * Followed the instruction on adafruit to solder the neessary parts 
  * Mounted the LCD display onto our Raspberry Pi 
  * Set up Pi for I2c
  * Realized had to enable I2C in ifconfig
  * Verified messages could be displayed using the example code provided

# Wednesday May 3, 2017

* LCD Display
  * Calibrated contrast 
  * Wrote our own sample text code to display current time at the press of a button
  * Code displays the current GMT time when the select button is pressed 
  * After a certain neumber of pressed the display will have text asking for new code

* Miscellaneous 
  * Fixed minor issue with bootup not emailing IP address to both parties
  * Prepared for Thursday's presentation

# Thursday May 4, 2017 

* Presentation 
  * Delivered presentation
  
# Monday May 8, 2017

* Fetching Coin data
  * free api on (Coin Market Cap)[https://coinmarketcap.com/api/]
  * using the `request` and `json` libraries we can fetch and parse API Data
  * our python script holds a dict in memory with our coins of interest
  * Script loops over our coins and updates their data

* LCD Display
  * using requests set up py script to display real time cryptocurrency values at the press of a button
  * currently just actively monitoring BTC and ETH
  * API has infinite requests, no key necessary 

# Tuesday May 9, 2017

* CoinWarz API
  * Generated API key for use on PI
  * Learned how to pull the information for specific coins and their mining profitabilities

* LCD Display
  * Learned how to created infinitely scrolling text across the screen
  * Wrote sample py files for having two lines of text
  * Will later modify this program to have static text in the frist row, scrolling text in the bottom

# Wednesday May 10, 2017

* Max Profit Alogrithm
  * Wrote py script to store current market value of monero in a csv file
  * Used cron to set market value to be stored every five minutes
  * Realized I did not use a full path in py file so the cronjob was not working 
  * Successfully managed to get an updating csv file with pricing information 
  * Researched possible hashrate of Raspberry Pi 3 and the projected profits of mining XMR/ETH/LTC

# Thursday May 11, 2017

* The max profit alogrithm catastrophe
  * Large setbacks in max profit alogrithm
  * Current difficulty may need devices to determine profit ratio, cannot determine from free APIs
  * Using json files to determine profit ratio in comparison to BTC for coins we will mine
  * Possible problem since we have a limited number of daily pings, and finite total pings 

# Friday May 12, 2017

* Picking up the pieces
  * Researching additional coins to mine in addition to Monero
  * Possibly Hirocoin and Fantomcoin
  * Cleaning up profit ratio API python code to be faster
  * Will purchas a bigger SD card to finally sycn monero to start mining

# Monday May 15, 2017

* New SD card
  * Configured new SD card, installed git, emacs, etc...
  * New card has 32GB in order to store the large blockchains
  * Dont fuck up equals sign formatting when writing network information!!!

* Mining Pool?
  * found mining pool software for cryptonote
  * (the software)[https://github.com/fancoder/cryptonote-universal-pool] would allow us to run our own mining pool
  * Could have my gaming computer mining as well several times faster than the pi could ever mine
  * Computers connected to the pool would not have to have anyything installed to join the pool

* LCD Display
  * Downloaded necessary tools to operate the LCD panel attached the the Pi
  * Verified systems were operational

# Tuesday May 16, 2017 

* Preparing for the end 
  * Finally got around to seperating our daily notes since we initially wrote together 
  * Decided on GitHub pages theme
  * Building pages 
  * Discussed specifically what we hope to accomplish by next Friday 
  * Currently waiting to finish Monero synch

* Monero Pool 
  * Began setting up mining pool on the Pi 
  * Cannot begin using until Monero synch is complete

# Wednesday May 17, 2017 

* Waiting for the synch to compelte 
  * Worked on GitHub pages 
  * Planned final video 