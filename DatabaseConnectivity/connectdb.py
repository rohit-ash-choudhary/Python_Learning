import mysql.connector;


mydb=mysql.connector.connect(host="localhost",user="root",password="test",database="test_python")

mycusor=mydb.cursor()

mycusor.excute("select * from customers")

result=mycusor.fetchone()


for i in result:
    print(i)