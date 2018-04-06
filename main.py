from gmail.connection import *
from gmail.get_emails import *
from mysql.crud import *
from mysql.structure import *

create_db = ""
while True:
    create_db = raw_input("Do you want to create the DB Structure ? (Yes/No): ")
    if create_db == "Yes" or create_db == "No":
        break

if create_db == "Yes":
    db_host = raw_input("Type the Database Instance Host (localhost, 127.0.0.1): ")
    db_user = raw_input ("Type the Database user: ")
    db_pass = raw_input ("Type your DB password: ")
    create_structure(db_user, db_pass, db_host)

else:
    db_host = raw_input("Type the Database Instance Host (localhost, 127.0.0.1): ")
    db_user = raw_input ("Type the Database user: ")
    db_pass = raw_input ("Type your DB password: ")


email = raw_input("Type an Email to Search: ")
password = raw_input("Type your Email Password: ")


def save_emails():
    login = gmail_login(email,password)
    dicionario = read_emails(login)
    print dicionario
    insert_table(db_host, db_user, db_pass, "gmailusers", dicionario)

def main():
    save_emails()

if __name__ == '__main__':
    main()
