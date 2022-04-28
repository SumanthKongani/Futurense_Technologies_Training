# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:25:22 2022

@author: suman
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass



#need to import from a csv file
emails_list = ['myselfsting@gmail.com', 'kryaanwill@gmail.com', 'sumanthkongani@gmail.com'] 
email_index = 0
sender_email = input('Enter your Email ID: ')
email_password = getpass.getpass('Enter passord: ')

body = ('''Greeting Mr. Kryaan,
Thank you for being with us.
Please find the encrypted password and the file attached.
Your encrypted password is: %s
''' %encrypted_pass_1)
receiver_email = emails_list[email_index]
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Sent the encrypted file'

message.attach(MIMEText(body, 'plain'))

pdfname = fpath

initial_path = r'F:\GitHub\Futurense_Technologies_Training' 
# open the file in bynary
binary_pdf = open(os.path.join(initial_path, pdfname), 'rb')

payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())

# enconding the binary into base64
encoders.encode_base64(payload)

# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)

#use gmail with port
session = smtplib.SMTP('smtp.gmail.com', 587)

#enable security
session.starttls()

#login with mail_id and password
session.login(sender_email, email_password)

text = message.as_string()
session.sendmail(sender_email, receiver_email, text)
session.quit()
print('Mail Sent')