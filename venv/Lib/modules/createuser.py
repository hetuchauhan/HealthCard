from datetime import datetime
from Lib.modules import hereismodules as him
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
mycursor = mydb.cursor()


def error():
    print("Error! Your input must be as instructed.\
          Restarting identity module. Re-enter the particulars.")
    create_identity()


def add_user_in_db(typ, name, age, gender, aadhaar, mobile, pin, sr_no=0, date=datetime.now(), hospital=0, hosp_id=0,
                   pharma_name=0, pharma_id=0):
    if typ == 1:
        date = datetime.now()
        mycursor.execute("create table if not exists patient (sr_no integer,\
                                                            name varchar(50) not null,\
                                                            age integer(3),\
                                                            gender varchar(1),\
                                                            aadhaar varchar(12) not null primary key,\
                                                            mobile varchar(10) not null,\
                                                            pin integer(6),\
                                                            date datetime)")
        mycursor.execute("insert into patient(name,age,gender,aadhaar,mobile,pin,date)\
                    values('" + str(name) + "','" + str(age) + "','" + str(gender) + "','" + str(aadhaar) + "','" + str(
            mobile) + "','" + str(pin) + "','" + date.strftime('%Y-%m-%d %H:%M:%S') + "')")

    elif typ == 2:
        date = datetime.now()
        mycursor.execute("create table if not exists doctor (sr_no integer,\
                                                            name varchar(50) not null,\
                                                            age integer(3),\
                                                            gender varchar(1),\
                                                            aadhaar varchar(12) not null primary key,\
                                                            mobile varchar(10) not null,\
                                                            pin integer(6),\
                                                            date datetime,\
                                                            hospital_name varchar(50),\
                                                            hospital_id varchar(50) not null)")

        mycursor.execute("insert into doctor(name,age,gender,aadhaar,mobile,pin,date,hospital_name,hospital_id)\
                            values('" + str(name) + "','" + str(age) + "','" + str(gender) + "','" + str(
            aadhaar) + "','" + str(mobile) + "','" + str(pin) + "','" + date.strftime(
            '%Y-%m-%d %H:%M:%S') + "','" + str(hospital) + "','" + str(hosp_id) + "')")

    else:
        date = datetime.now()
        mycursor.execute("create table if not exists pharma (sr_no integer,\
                                                            name varchar(50) not null,\
                                                            age integer(3),\
                                                            gender varchar(1),\
                                                            aadhaar varchar(12) not null primary key,\
                                                            mobile varchar(10) not null,\
                                                            pin integer(6),\
                                                            date datetime,\
                                                            pharma_name varchar(50),\
                                                            pharma_id varchar(50) not null)")
        mycursor.execute("insert into pharma(name,age,gender,aadhaar,mobile,pin,date,pharma_name,pharma_id)\
                    values('" + str(name) + "','" + str(age) + "','" + str(gender) + "','" + str(aadhaar) + "','" + str(
            mobile) + "','" + str(pin) + "','" + date.strftime('%Y-%m-%d %H:%M:%S') + "','" + str(
            pharma_name) + "','" + str(
            pharma_id) + "')")
    mydb.commit()


def create_identity():
    him.connectdb()
    # Collecting details
    name1 = input("Enter your name: ")
    try:
        age = int(input("Enter your age(in numbers): "))
    except:
        error()
    gender = input("Enter your gender(M/F/O): ")
    if him.is_correct_input("gender", gender) == True:
        pass
    else:
        error()
    aadhaar = int(input("Enter your 12 digit Aadhaar Number: "))
    if him.is_correct_input("aadhaar", aadhaar) == True:
        pass
    else:
        error()
    mobile = int(input("Enter your mobile number: "))
    if him.is_correct_input("mob", mobile) == True:
        pass
    else:
        error()
    pin = int(input("Zip Code: "))
    if him.is_correct_input("zip", pin) == True:
        pass
    else:
        error()
    typ = int(input("Enter your type(1.Patient/2.Doctor/3.Pharmacy)(Type only integer): "))

    if typ == 1:
        user = " Name: " + name1 + " Age: " + str(age) + " Gender: " + gender + " Aadhaar: " + str(
            aadhaar) + " Mobile: " + str(mobile) + " PIN: " + str(pin)
        add_user_in_db(typ, name1, age, gender, aadhaar, mobile, pin)  # adding in db

    elif typ == 2:
        hospital = input("Enter your hospital name in full: ")
        hosp_id = input("Enter your registered id/affliation number: ")
        user = " Name: " + name1 + " Age: " + str(age) + " Gender: " + gender + " Aadhaar: " + str(
            aadhaar) + " Mobile: " + str(mobile) + " PIN: " + str(
            pin) + " Hospital name: " + hospital + " Hospital ID: " + str(hosp_id)
        add_user_in_db(typ, name1, age, gender, aadhaar, mobile, pin, hospital, hosp_id)  # adding in db

    else:
        pharma_name = input("Enter your pharmacy shop name in full: ")
        pharma_id = input("Enter your registered id/affliation number: ")
        user = " Name: " + name1 + " Age: " + str(age) + " Gender: " + gender + " Aadhaar: " + str(
            aadhaar) + " Mobile: " + str(mobile) + " PIN: " + str(
            pin) + " Pharma name: " + pharma_name + " Pharma ID: " + str(pharma_id)
        add_user_in_db(typ, name1, age, gender, aadhaar, mobile, pin, pharma_name, pharma_id)  # adding in db

    # encryption
    key = him.encrypt_key()
    enc_user = him.encrypt(user, key)
    key1 = str(key) + " " + name1 + " " + str(aadhaar)
    print(user, " Key: ", key,"data: ",enc_user)

    # creating a qrcode and stroring data in it
    him.createqr(enc_user, aadhaar)
    him.createqrkey(key1, aadhaar)
