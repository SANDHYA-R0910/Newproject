import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="")
# print(mydb)

cursor = mydb.cursor()
# cursor.execute("create database sairam1")
# cursor.execute("show databases")
#s = "create table sairam1.ineuron1(employe_id int  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int , emp_attendence int)"
#cursor.execute(s)

# q2 = cursor.execute("select * from sairam1.ineuron1")
# print(q2)
m = "insert into sairam1.ineuron1 values(1,'sai','sai@gmail.com',100,30)"
cursor.execute(m)
mydb.commit()
