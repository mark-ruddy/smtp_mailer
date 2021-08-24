smtp_addr = 'smtp.gmail.com'      # Gmails SMTP server
smtp_port = 587                   # SMTP supported port for Gmail

attachments = [                   # Locations of Attachments, relative or full path, leave as empty [] for no attachments
    'important.pdf',
    'cat.png',
    '/opt/opt_cat.jpeg',
]

which_sender_to_use = 0           # Leave at 0 to use the first sender in dictionary
senders = {
    'user@gmail.com':'PASSWORD',  # Your actual email and password from provider
    'user1@gmail.com':'PASSWORD', # This is not particularly secure, consider using a throw-away account or encryption
}

receivers = {                     # The List of recipients, mail will go to each.
    'user@protonmail.com':'User', # <receiver_email>:<receiver_actual_name(Optional - leave as "" for no-name)>
    'john@gmail.com':'John Smith',
    'sparrow1828@outlook.com':'Captain Jack Sparrow',
}

subject = 'Change subject here'

# generateMsg should return the text content of the email
# by default i is passed as the iteration of how many emails are sent
def generateMsg(i):
    return f'I have sent {i+1} messages'

