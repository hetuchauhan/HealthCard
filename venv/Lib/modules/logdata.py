def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st

def logdata(user,typ):
    dec_user=convertTuple(user)
    from datetime import datetime
    import mysql.connector
    date = datetime.now()
    mydb = mysql.connector.connect(host="localhost", user="root", password="hetu123456", database="patients")
    mycursor = mydb.cursor()
    mycursor.execute("create table if not exists logbook(sr_no integer auto_increment,\
                                                        data text null,\
                                                        date datetime,\
                                                        typ varchar(12),\
                                                        INDEX(`sr_no`))")
    mycursor.execute("insert into logbook(data,date,typ)\
                            values('" + str(dec_user) + "','" + date.strftime('%Y-%m-%d %H:%M:%S') + "','" + typ + "')")
    print("session logged!")
    mydb.commit()