import pytest

from gmail.connection import *
from mysql.crud import *

def test_gmail_connection():
    mail = gmail_login("lucas@gmail.com","testeclasss")
    assert mail == False
