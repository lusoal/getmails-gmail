import smtplib
import time
import imaplib
import email
from datetime import datetime

from mysql.crud import *

def read_emails(mail, session):
    #dicionario = {"Email":[],"Subject":[],"Time":[]}
    mail.select('inbox')
    # type, data = mail.search(None, 'ALL')
    #change to ALL to search inside all of your email Box, or Specify a Date
    type, data = mail.search(None, '(SINCE "01-Apr-2018")')

    ids = data[0]
    id_list = ids.split(" ")

    for ids in id_list:
        typ, data = mail.fetch(ids, '(RFC822)' )
        for response_part in data:
            if isinstance(response_part, tuple):
                b = email.message_from_string(response_part[1])
                if b.is_multipart():
                    for part in b.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))

                        # skip any text/plain (txt) attachments
                        if ctype == 'text/plain' and 'attachment' not in cdispo:
                            body = part.get_payload(decode=True)  # decode
                            if "DevOps" in body or "DevOps" in b['subject']:
                                email_from = (((str(b['from']).split(" ")).pop()).replace("<","")).replace(">","")
                                subject = b['subject']

                                list_string = (b['date'].split(" "))
                                list_string.pop(len(list_string)-1)
                                list_string.pop(0)
                                list_string = str('-'.join(list_string)).replace(",","")
                                try:
                                    data = datetime.strptime(list_string, "%d-%b-%Y-%H:%M:%S")
                                except:
                                    data = list_string
                                insert_emails(session, data, email_from, subject)
                else:
                    body = b.get_payload(decode=True)
    
