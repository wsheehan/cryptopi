
'''
In order to send on boot edit the 
/etc/rc.local file to call this script
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import socket

# get ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
ip_address = s.getsockname()[0]

fromaddr = "cryptorasberrypi@gmail.com"
toaddr = "wsheehan@bates.edu"

msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Booted Pi's IP"
body = "This is our pi's IP address: " + ip_address
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cryptoraspberrypi@gmail.com", "ethereum")
text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)
server.quit()
