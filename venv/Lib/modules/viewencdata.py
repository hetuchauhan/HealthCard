from Lib.modules import hereismodules as him, logdata as ld
from datetime import datetime
him.imports()
import mysql.connector

def error():
    print("Error! Your input must be as instructed.\
          Restarting identity module. Re-enter the particulars.")
    frontendinput()

def frontendinput():

    key=input("Enter the key provided at the time of registration\
              or scan the QR code provided.: ")
    data=input("Enter the data string or scan the relevant image.: ")

    byt=bytes(data,'utf-8')
    try:
        dec_user=him.decrypt(key,byt)
    except:
        error()
    ld.logdata(dec_user, 'endusersearch')
    print(dec_user)

