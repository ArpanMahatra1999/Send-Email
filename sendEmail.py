import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from sense_hat import SenseHat
import time
from time import asctime

sense = SenseHat()

fromaddr = "arpanmahatra1999@gmail.com"
toaddr = "sapkotariddhi9@gmail.com"
msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Temp Rasp"

t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

bg = [0, 0, 100]
tc = [200, 200, 0]

message = "T = {0} P = {1} H = {2} .".format(t, p, h)
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 25)
server.starttls()
server.login(fromaddr, 'mygmailpassword')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()