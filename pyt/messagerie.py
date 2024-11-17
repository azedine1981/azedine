# coding: utf-8

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'AAA@gmail.com'
msg['To'] = 'YYY@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('AAA@gmail.com', 'PASSWORD')
mailserver.sendmail('AAA@gmail.com', 'AAA@gmail.com', msg.as_string())
mailserver.quit()
