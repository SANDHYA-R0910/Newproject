import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="")
cursor = mydb.cursor()
s = "insert into sairam1.ineuron1 values(1,'sai','sai@gmail.com',100,30)"
cursor.execute(s)
#"insert into sudhanshu.ineuron1 values(101 , 'sudhanshu kumar', 'sudhanshu@ineuron.ai' ,100 , 30)"
mydb.commit()