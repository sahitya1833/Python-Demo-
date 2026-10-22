import pymysql
connection =pymysql.connect(host = "localhost", port= 3306, user= "root", password = "root" , db = "curd_operations")
cursor =connection.cursor()
sql = "create table student (id int primary key, roll_no int, name varchar(20), city varchar(20))"
cursor.execute(sql)
connection.commit()
connection.close()
print("table created successfully")
