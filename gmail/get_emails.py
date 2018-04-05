import smtplib
import time
import imaplib
import email
from datetime import datetime

def read_emails(mail):
    dicionario = {"Email":[],"Subject":[],"Time":[]}
    mail.select('inbox')
    type, data = mail.search(None, 'ALL')
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
                                dicionario['Email'].append((((str(b['from']).split(" ")).pop()).replace("<","")).replace(">",""))
                                dicionario['Subject'].append(b['subject'])
                                # datetime_object = datetime.strptime(str( b['date']), '%b %d %Y %I:%M%p')
                                list_string = (b['date'].split(" "))
                                list_string.pop(len(list_string)-1)
                                list_string.pop(0)
                                list_string = str('-'.join(list_string)).replace(",","")
                                data = datetime.strptime(list_string, "%d-%b-%Y-%H:%M:%S")
                                dicionario['Time'].append(str(data))


                else:
                    body = b.get_payload(decode=True)
    return dicionario                        
                    # print body
                    # if "DevOps" in msg:
                    #
                    #     email_from = msg['from']
                    #     print email_subject
                    # #
                    # print 'From : ' + email_from. + '\n'
                    # print 'Subject : ' + email_subject + '\n'
