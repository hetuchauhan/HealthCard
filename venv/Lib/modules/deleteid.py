def deleteid(typ,data):
    from Lib.modules import hereismodules as him

    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    mycursor = mydb.cursor()

    if typ == 1:

        statement = """select * from reg where aadhaar= %s"""
        mycursor.execute(statement, (data,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)

        statement2 = """delete from reg where aadhaar= %s"""
        mycursor.execute(statement2,(data,))
        print("rec deleted!")
        returncode=200
        mydb.commit()
        return records, returncode

    elif typ == 2:

        statement = """select * from reg where mobile= %s"""
        mycursor.execute(statement, (data,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        for i in records:
            print(i)
        statement2 = """delete from reg where mobile= %s"""
        mycursor.execute(statement2, (data,))
        print("rec deleted!")
        returncode = 200
        mydb.commit()
        return records, returncode
    elif typ == 3:


        statement = """select * from reg where name= %s"""
        mycursor.execute(statement, (data,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        for i in records:
            print(i)
        statement2 = """delete from reg where name= %s"""
        mycursor.execute(statement2, (data,))
        print("rec deleted!")
        returncode = 200
        mydb.commit()
        return records, returncode
    elif typ==4:
        quit()
    else:
        print("invalid input!")
    mydb.commit()

