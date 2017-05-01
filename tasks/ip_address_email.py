
'''
In order to send on boot edit the 
/etc/rc.local file to call this script
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import socket
import os

email_pass = os.environ.get('EMAIL_PASS')

# get ip address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
ip_address = s.getsockname()[0]

fromaddr = "cryptorasberrypi@gmail.com"
tolist = ["wsheehan@bates.edu", "chollima@bates.edu"]

msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = ", ".join(tolist)
msg["Subject"] = "Booted Pi's IP"
body = "This is our pi's IP address: " + ip_address
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cryptoraspberrypi@gmail.com", email_pass)
text = msg.as_string()

server.sendmail(fromaddr, tolist, text)
server.quit()
