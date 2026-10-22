import pymysql
connection = pymysql.connect(host = "localhost",port =3306, user = "root", password= "root", db ="curd_operations")
cursor = connection.cursor()
sql = "insert into student values(1,101,'jay kumar', 'indore')"
sql1 = "insert into student values(2,102,'khushi patel', 'bhopal')"
cursor.execute(sql)
cursor.execute(sql1)
connection.commit()
connection.close()
print("data added successfully")
