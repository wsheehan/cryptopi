# Wednesday April 26

* kai told us about github pages
* Completed cron datetime task
  * Used crontab -e to edit system cron jobs
  * Needed new line at end of file to run
  * reference cron syntax and determined correct way of assigning a once per minute task `* * * * *`

### Created git tutorial for craig for our workflows

(This is the workflow I've used in my teams before, it is a simple one but one that works for a small team)

To pull down newest version
```
git pull
```
To check your local changes
```
git status
```

Start new branch for development
```
git checkout -b <branch_name>
```

To check difference on local file vs master
```
git diff <file_name>
```

To add a files changes to staging
```
git add <file_name> 
git add -A # to add all changes
```

Commit changes
```
git commit -m "Message about what you did"
```

push requested changes
```
git push origin <branch_name>
```

# April 27

* Email Task
  * use socket to retrieve IP address
  * use pythons smtp server to send mail
  * new email is cryptoraspberrypi@gmail.com
  * send on boot from `/etc/rc.local`
  * Final file in `tasks/ip_address_email.py`

### Project planning
* created schematic of services
* checked docker images of each coin only found one for monero
* lcd display may force us to use python and not node.js or ruby 

![Alt text](schematic.jpeg)

# May 1

* Initial Raspberry Pi Setup 
  * Installed heatsinks onto Raspberry Pi 
  * Used clearpass to register our device 
  * Successfully SSH'd into our Pi and installed emacs and Git 
  * Copied over py file to email us the IP address upon booting up
  * refactored IP adress file to not store password in plain text 

* LCD Display 
  * Found online manual to connect LCD display parts 
  * Verified all parts were accounted for

# May 2, 2017

* Building the LCD Display 
  * Followed the instruction on adafruit to solder the necessary parts 
  * Mounted the LCD display onto our Raspberry Pi (after tons of soldering) 
  * Set up Pi for I2c
  * Verified messages could be displayed

# May 3, 2017

* Miscellaneous 
  * Fixed minor issue with bootup not emailing IP address to both parties
  * used docopt so we can pass password as command line arg to python script
  * Prepared for Thursday's presentation

* Docker config
  * installed docker on the pi
  * Researched docker images for cpu miners
  * Found [Monero Miner](https://github.com/OhGodAPet/cpuminer-multi)
  * Need to determine if GPU or CPU mining will be more efficient with ethereum
  * Litcoin has some resources but fairly scarce

# May 4, 2017

* Presentations...

# May 8, 2017

* Fetching Coin data
  * free api on [Coin Market Cap](https://coinmarketcap.com/api/)
  * using the `request` and `json` libraries we can fetch and parse API Data
  * our python script holds a dict in memory with our coins of interest
  * Script loops over our coins and updates their data

* Docker API
  * downloaded docker api client for python
  * wrote example docker api script

# May 9, 2017

* Monero Config
  * Found out that the monero miner we found was not compatible with ARM architecture
  * Found CPU info at `/proc/cpuinfo` it is ARMv7 
  * Downloaded ARMv7 binaries and copied to the pi with `scp -r`
  * Created monero wallet by running `./monero-wallet-cli` executable
  * In order to use wallet cli entire blockchain must be synced
  * Will need to sync on pi overnite, will need to track how much space it is using

* Eth Config
  * Downloaded ARMv7 binary and copied to the pi
  * We are using `geth` which is the go implementation of ethereum for it has CPU mining
  * Will need to create an ether wallet

# May 10, 2017

* Cryptonote
  * Realization that coins on the cryptonote algo are likely the only ones we can mine
  * Upon research monero remains a good option as it is on cryptonote
  * bytecoin, the OG cryptonote currency also seems appealing

# May 11

* The bytecoin compilation catastrophe
  * Large setbacks in compiling bytecoin
  * bytecoin does not roll its own armv7 version therefore the only option is building from source
  * This requires cmake, gcc, and boost all of which I installed
  * A thread error is being called and about a dozen stack overflow answers later I have been unable to compile successfully
  * The error being raised relateds to pthread
  * May have to just scrap bytecoin

# May 12, 2017

* Picking up the pieces
  * Researching additional coins to mine in addition to Monero and not bytecoin
  * Possibly Hirocoin and Fantomcoin
  * Cleaning up profit ratio API python code to be faster
  * Might need a bigger SD card

# May 15

* New SD card
  * Configured new SD card, installed git, emacs, etc...
  * New card has 32GB in order to store the large blockchains
  * Dont fuck up equals sign formatting

* Monero Config
  * Copied over monero binary
  * Restarted sync, seems to be moving faster
  * Running sync in background using screen
  * good screen [reference](https://www.howtoforge.com/linux_screen)

* Mining Pool?
  * found mining pool software for cryptonote
  * [the software](https://github.com/fancoder/cryptonote-universal-pool) would allow us to run our own mining pool

# May 16

* Pool config
  * Downloaded redis via `sudo apt-get install redis-server`
  * Redis is a data structure storage server that is incredibly fast & used by pool software
  * install nodejs as per their website [installation](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions)