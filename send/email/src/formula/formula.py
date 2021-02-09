#!/usr/bin/python3
import email_to

def run(sender_email, sender_password, receiver_email, subject, message):

    try:
        server = email_to.EmailServer(
            'smtp.gmail.com',
            587,
            sender_email,
            sender_password
            )
        
        server.quick_email(
            receiver_email, 
            subject,
            ["", message],
            style = 'h1 {color: blue}'
            )
    except:
        print("❌ The message couldn't be sent to {}".format(receiver_email)) 
    
    print("✅ The message has been successfully sent to {}".format(receiver_email)) 