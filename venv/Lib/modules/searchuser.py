def searchuser(pref,data):
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    mycursor = mydb.cursor()

    if pref == 1:

        statement = """select * from reg where aadhaar= %s"""
        mycursor.execute(statement, (data,))
        records = mycursor.fetchall()
        print("Total no of rows in table: ", mycursor.rowcount)
        return records, mycursor.rowcount

    elif pref == 2:

        statement = """select * from reg where mobile= %s"""
        mycursor.execute(statement, (data,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        return records, mycursor.rowcount

    elif pref == 3:

        statement = """select * from reg where name= %s"""
        mycursor.execute(statement, (data,))
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        return records, mycursor.rowcount

    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    mycursor = mydb.cursor()
