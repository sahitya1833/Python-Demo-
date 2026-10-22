import pymysql
connection =pymysql.connect(host="localhost", port = 3306, user ="root", password ="root",db ="curd_operations")
cursor = connection.cursor()
sql = "update student set name = 'jadish kumar' where id = 1"
cursor.execute(sql)
connection.commit()
print("Record update successfully")

