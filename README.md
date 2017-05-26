# Introduction and Motivation 
This guide will describe to how to use a Raspberry Pi as a cryptocurrency miner.  The Pi will have a miniature LCD display attached that will have various mining information shown.  Additionally, readers will learn how to set up a cryptocurrency pool on their Pi that could then be connected to via any device. The final product can be seen below: 

**Insert finished product here**

Please note that mining with a Raspberry Pi alone (without having additionally systems set up through a pool as we do) will likely never result in any profits. This is first and foremost an educational project. The advantages of using a Pi is that we can always have it turned on devoting processing power to mining and that we can attach a miniature LCD display that is always displaying information about the mining process. Additionally, since the Pi has built in Wifi it would be possible to attach a portable power supply and take the Pi around to show off how cool the LCD display is! 

So with that in mind let's get started! 

# Materials and Costs 
**Raspberry Pi**

Clearly the most vital part of this project is the Raspberry Pi. We recommend purchasing the latest model Pi off of the Adaruit website. You can prucahse the model we used, Rapsberry Pi 3 - Model B, [here](https://www.adafruit.com/product/3055).

Cost: $39.95 + Shipping

**Micro SD Card**

Don't be tempted to get a small 4GB or 8GB like we originally did. Synchronizing the blockchain will take a signifigant amount of memory. Go for a 16GB or 32GB if you wish to mine several cryptocurrencies. Eventually we went with [this](http://www.bestbuy.com/site/sandisk-pixtor-advanced-32gb-microsdhc-uhs-i-memory-card-red-gold/7801066.p?skuId=7801066&extStoreId=&ref=212&loc=1&ksid=cfee5b1a-3e22-4387-b064-eefd78af148e&ksprof_id=14&ksaffcode=pg174626&ksdevice=c&lsft=ref:212,loc:2) Sandisk card. 

Cost: $29.99

**LCD Display**

Not necessary but definitely a very cool addition to the project is the Adafruit Blue & White 16x2 LCD + Keypad kit. Snag it on amazon prime [here](https://www.amazon.com/ADAFRUIT-INDUSTRIES-1115-KEYPAD-RASPBERRY/dp/B00DK2A1KE/ref=sr_1_14?ie=UTF8&qid=1495047907&sr=8-14&keywords=adafruit+lcd+display).

Cost: $19.91

**Total Costs**
~$100.00 

# Raspberry Pi Configuration 
The first step in configuring your Raspberry Pi is to hook it up to an external monitor and keyboard. Boot up the Pi and connect to your wifi hotspot (or ethernet). Obtain the IP address. Go into the ifconfig and make sure to parition the micro SD card to use the entire memory. You will also want to go ahead and enable SSH and I2C while you are in the ifconfig. If this is your first time configuring a Raspberry Pi we recommend you follow this [guide](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration/overview) by Adafruit.  

With this complete you are all set to SSH into your Pi and get to work. 

# Installing the LCD Display 

If you decide to forego purchasing the LCD display skip this section. Otherwise put your solder hat on and getting ready to spend the next hour or so soldering. We are not going to go into specifics of how to install the board since Adafruit has a perfectly written guide [here](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/assembly).

Some notes from our experience putting it together:
* Solder outside. The fumes will get to you 
* Absolutely do not forget to place the electrical tape on the USB connection
* It is highly likely the contrast will not be calibrated correctly. Use a small screwdriver and twist the orange button  until the text is visible 
* Do not press the buttons too hard. As you will learn the board is not supported properly on one of the corners once installed onto the Pi  

# Monero 
For our project we have deicded to mine Monero. This is primarilly because Monero is a CPU intensive cryptocurrency to mine. Additionally, when we were beginning the project in May 2017 there was a lot hype around it and it's value was skyrocketing. Do some research. There are hundreds of coins to choose from. 


# Pooling 

For our pool we have decided to leverage an [open source pool](https://github.com/zone117x/node-cryptonote-pool) designed for cryptonote based coins. The pool has tons of features that we are really just scraping the surface of, however there are a couple important ones to note. The ability to load balance mining from faster cpus vs. our pi or a phone etc... Second the pool rolls its own ajax api which we can query and then display mining and pool data on the LCD display.

What is a mining pool?

Mining pools allow for external mining to join a group of miners and contribute their share of mining power. Pools are appealing to many because it means avoiding downloading coin binaries and setting up a full node. Most professional miners mine in pools so as to increase block award probability. Setting up a pool on our pi allows us to leverage the pi's ability to be always running, while also allowing stronger CPU's to attach and possibly mine non-trivial amounts.

Setup
* Install redis `sudo apt-get install redis-server`, redis is a key value store that is lightning fast
* Install nodejs [instructions](https://nodejs.org/en/download/package-manager/)
* Install libssl and Boost `sudo apt-get install libssl-dev libboost-all-dev`

Running
* node init.js

# Preliminary Resutls and Conclusion 

some graphs or something here would be really nice...

The links to our individual daily logs can be found here: and here: . 

# Challenges

**Difficulty of coins**
Quickly it became apparent that most coins were going to be completely unfeasible on the pi, two of our originals, ethereum and litecoin were among said coins. This brought us to the crytonote algorithm. The only mainstream coins that are CPU mineable feasibly are cryptonote based coins. Monero is the largest with Bytecoin also managing a large market cap. Monero rolls an ARMv7 binary, Bytecoin however... did not. Before the pooling pivot was made we spent a significant amount of time trying to build bytecoin from source on our pi, to no avail. Other cryptonote coins have very similar achitectures to bytecoin so we could not run them either. This lead us to focusing just on Monero and moving towards pooling.

**Disk Space**
On the monero website, the monero blockchain is described as 'a couple gigs', therefore we assumed that our 8GB SD card would be sufficient. After about half of a sync, a quick `df` showed we were quickly approaching our limit. Therefore quite late in the game we had to buy a new 32GB SD card to adequately hold the monero blockchain.

**Synchronization**
In order to mine and run a node, the ENTIRE history of monero must be stored and verified in the form of the blockchain. This is what makes cryptocurrencies work, a shared understanding of the blockchain. However, this synchronization is not fast. In our first sync try on the 32GB card we tried to sync from scratch, and made it all the way to 1200001 out of ~13100000 when a power flicker disrupted the sync. Additionally after the power outage we were not entirely clear that we could not resume, losing more time. In a last ditch effort with only 3 days left we tried a different sync technique where you download the 'raw' blockchain and then have a monero import program verify *every*single block. This too has proved slow, possibly slower than from scratch. As of 5/26 in the morning we sit at 1150000 out of ~131000. Close, but not quite enough to have a functioning miner/pool as of yet. 

* Network issues - slow, potentiallydownload block on school netowrks 
* Size Constraints - downloading the blockchains takes a lot of time and memory 
* Mining power - Raspberry Pi alone with never accomplish anything signifigant, unless working with free elecetricty in which case it will still take considerable time to break even 



# Video Demonstration 

Lets make a brief two minute video that has both of us in it a shows the information the Pi has.

30 seconds brief introduction to what the raspberry Pi does 
30 seconds using desktop to join the pool 
30 seconds showing the information being displayed on the LCD display 
