import pymysql
connection =pymysql.connect(host = "localhost", port =3306, password= "root", user="root", db = "curd_operations")
cursor = connection.cursor()
sql = "delete from student where id=1"
cursor.execute(sql)
connection.commit()
connection.close()
print("record deleted successfully")

