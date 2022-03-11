def deleteid():
    from Lib.modules import hereismodules as him

    import mysql.connector

    pref = int(input("How would you like to delete the record\n1. By Aadhaar No.\n2. By Mobile\n3. By Name\n4. Exit\n--->"))

    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    mycursor = mydb.cursor()

    if pref == 1:

        aadhaar = input("Enter Aadhaar No.: ")
        a = him.is_correct_input("aadhaar", aadhaar)
        if a == True:
            pass
        else:
            him.error()
        statement = """select * from reg where aadhaar= %s"""
        mycursor.execute(statement, (aadhaar,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        for i in records:
            print(i)

        statement2 = "delete from reg where aadhaar= %s"
        mycursor.execute(statement2, (aadhaar,))
        print("rec deleted!")

    elif pref == 2:

        mob = input("Enter Mobile No.: ")
        a = him.is_correct_input("mob", mob)
        if a == True:
            pass
        else:
            him.error()
        statement = """select * from reg where mobile= %s"""
        mycursor.execute(statement, (mob,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        for i in records:
            print(i)
        statement2 = """delete from reg where mobile= %s"""
        mycursor.execute(statement2, (mob,))
        print("rec deleted!")

    elif pref == 3:

        name1 = input("Enter Name: ")
        statement = """select * from reg where name= %s"""
        mycursor.execute(statement, (name1,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        for i in records:
            print(i)
        statement2 = """delete from reg where name= %s"""
        mycursor.execute(statement2, (name1,))
        print("rec deleted!")
    elif pref==4:
        quit()
    else:
        print("invalid input!")
        deleteid()
    mydb.commit()

