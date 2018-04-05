from gmail.connection import *
from gmail.get_emails import *
from crud.crud import *

def save_emails():
    login = gmail_login("","")
    dicionario = read_emails(login)
    print dicionario
    insert_table("", "", "", "", dicionario)

def main():
    save_emails()

if __name__ == '__main__':
    main()
