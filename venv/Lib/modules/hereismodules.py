def hereismodules():
    # importing the sys module
    import sys

    # inserting the mod.py directory at 
    # position 1 in sys.path
    sys.path.insert(1, 'D:/Python projects/base/modules')


def imports():
    import pyqrcode
    import png
    from pyqrcode import QRCode
    import datetime
    import mysql.connector


from datetime import date
import mysql.connector
from cryptography.fernet import Fernet


def connectdb():
    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    print(mydb)
    mycursor = mydb.cursor()
    a = mycursor
    return a


def dbforpyextscript():
    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    return mydb


def encrypt_key():
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    return key


def encrypt(data, key):
    from cryptography.fernet import Fernet
    fernet = Fernet(key)
    enc_data = fernet.encrypt(data.encode())
    return enc_data


def createqr(data, file_name):
    import pyqrcode
    import png
    from pyqrcode import QRCode
    qr = pyqrcode.create(data)
    qr.png(format(file_name) + ".png", scale=100)


def createqrkey(data, file_name):
    import pyqrcode
    import png
    from pyqrcode import QRCode
    qr = pyqrcode.create(data)
    qr.png(format(file_name) + " key.png", scale=100)


def is_correct_input(que, data):
    data = str(data)
    if que == "mob":
        if len(data) == 10:
            return True
        else:
            return False
    elif que == "aadhaar":
        if len(data) == 12:
            return True
        else:
            return False
    elif que == "zip":
        if len(data) == 6:
            return True
        else:
            return False
    elif que == "gender":
        if data in ["m", "M", "f", "F", "o", "O"]:
            return True
        else:
            return False
    else:
        pass
