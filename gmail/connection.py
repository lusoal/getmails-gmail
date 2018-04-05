import smtplib
import time
import imaplib
import email

def gmail_login(user, password):
    try:
        mail = imaplib.IMAP4_SSL("smtp.gmail.com")
        mail.login(user, password)
        return mail
    except Exception as e:
        print e
        return False
