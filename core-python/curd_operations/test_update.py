import pymysql
connection =pymysql.connect(host="localhost", port = 3306, user ="root", password ="root",db ="corepython")
cursor = connection.cursor()
sql = "update marksheet set name = 'anuj' where id = 21"
cursor.execute(sql)
connection.commit()
print("Record update successfully")

