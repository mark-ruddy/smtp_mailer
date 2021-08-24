import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText           
from email.utils import formataddr            
from email.mime.base import MIMEBase         
from email import encoders 

import config


smtp_client = smtplib.SMTP(config.smtp_addr, config.smtp_port)
# smtp_client.set_debuglevel(True) # Uncomment for verbose logging in console

smtp_client.ehlo() 
smtp_client.starttls() 
smtp_client.ehlo() 

# Grab our username and password from config.py
username = list(config.senders.keys())[config.which_sender_to_use]
password = config.senders[username]

smtp_client.login(username, password) # Attempt to login to our email account

def makeEmailMessage(receiver_name, receiver_email, subject, attachments=None, extra=''):
    # Make body using f-string, extra is an optional parameter to include text in body.
    body = f"""Hi {receiver_name},

{extra}"""
    msg = MIMEMultipart() # Use MIME standard for email formatting
    msg['From'] = username 
    msg['To'] = formataddr((receiver_name, receiver_email)) 
    msg['Subject'] = subject
    body = MIMEText(body)
    # This does not "attach" the body text as a file, it is added to the text content of email
    msg.attach(body)
 
    if attachments is None:
        attachments = []

    # Every file in attachments will be added to msg using standard email encoding
    # The files local name will be used to name it
    for file in attachments:
        attach_file = open(file, 'rb') # open in binary mode
        email_file = MIMEBase('application', 'octate-stream')
        email_file.set_payload((attach_file).read())
        encoders.encode_base64(email_file)

        email_file.add_header('Content-Disposition', 'attachment', filename=file)
        msg.attach(email_file) 

    return msg

for i, (receiver_email, receiver_name) in enumerate(config.receivers):
    msg = makeEmailMessage(receiver_name, receiver_email, config.subject, config.attachments, config.generateMsg(i))
    smtp_client.send_message(msg, username, receiver_email)
    print(f'{i}: email sent to {receiver} from {username}')

