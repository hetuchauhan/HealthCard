from Lib.modules import hereismodules as him
from datetime import datetime
him.imports()
import mysql.connector

def error():
    print("Error! Your input must be as instructed.\
          Restarting identity module. Re-enter the particulars.")
    frontendinput()

def frontendinput():
    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    mycursor = mydb.cursor()
    key=input("Enter the key provided at the time of registration\
              or scan the QR code provided.: ")
    data=input("Enter the data string or scan the relevant image.: ")

    byt=bytes(data,'utf-8')
    try:
        dec_user=him.decrypt(key,byt)
    except:
        error()
    date = datetime.now()

    mycursor.execute("create table if not exists logbook (sr_no integer,\
                                                                data text null,\
                                                                date datetime)")
    mycursor.execute("insert into logbook(data,date)\
                        values('" + str(dec_user) + "','" + date.strftime('%Y-%m-%d %H:%M:%S') + "')")
    print(dec_user)
    print("session logged!")
