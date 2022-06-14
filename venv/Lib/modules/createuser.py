from datetime import datetime
from Lib.modules import hereismodules as him
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
mycursor = mydb.cursor()


def error():
    print("Error! Your input must be as instructed.\
          Restarting identity module. Re-enter the particulars.")
    create_identity()

def add_user_in_db(name, age, gender, aadhaar, mobile, pin,dep,sr_no=0, date=datetime.now()):
    date = datetime.now()
    print(name, 'here')
    print(age, 'here')
    mycursor.execute("create table if not exists reg (sr_no integer,\
                                                        name varchar(50) not null,\
                                                        age integer(3),\
                                                        gender varchar(1),\
                                                        aadhaar varchar(12) not null primary key,\
                                                        mobile varchar(10) not null,\
                                                        pin integer(6),\
                                                        date datetime,\
                                                        department varchar(50) not null)")

    mycursor.execute("insert into reg(name,age,gender,aadhaar,mobile,pin,date,department)\
                    values('" + str(name) + "','" + str(age) + "','" + str(gender) + "','" + str(aadhaar) + "','" + str(
        mobile) + "','" + str(pin) + "','" + date.strftime('%Y-%m-%d %H:%M:%S') + "','" + str(
            dep) + "')")
    mydb.commit()

def create_identity(typ,name1="abc",age="0",gender="0",aadhaar=0,mobile=0,pin=0,dep=0):
    him.connectdb()
    if typ==1:

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
        dep = input("Enter your type(1.Patient/2.Doctor/3.Pharmacy)(Type in words): ")

        user = " Name: " + name1 + " Age: " + str(age) + " Gender: " + gender + " Aadhaar: " + str(
            aadhaar) + " Mobile: " + str(mobile) + " PIN: " + str(pin) + "dep" + str(dep)
        add_user_in_db(name1, age, gender, aadhaar, mobile, pin, dep)  # adding in db

    elif typ==2:
        user = " Name: " + name1 + " Age: " + str(age) + " Gender: " + gender + " Aadhaar: " + str(
                aadhaar) + " Mobile: " + str(mobile) + " PIN: " + str(pin) + "dep" + str(dep)
        add_user_in_db(name1, age, gender, aadhaar, mobile, pin,dep)  # adding in db

        # encryption
    key = him.encrypt_key()
    enc_user = him.encrypt(user, key)
    key1 = str(key) + " " + name1 + " " + str(aadhaar)
    print(user, " Key: ", key,"data: ",enc_user)

        # creating a qrcode and stroring data in it
    him.createqr(enc_user, aadhaar)
    him.createqrkey(key1, aadhaar)