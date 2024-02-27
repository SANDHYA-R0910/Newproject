import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="")



def createCursor():
    return mydb.cursor()

cursor = createCursor()

def commit():
    return mydb.commit()

def close():
    return cursor.close()