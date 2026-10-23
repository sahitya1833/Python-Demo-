import pymysql
connection =pymysql.connect(host= "localhost", port= 3306,user= "root",password= "root",db = "curd_operations")
cursor =connection.cursor()
#sql ="create table practice(id int primary key, names varchar(20), class int, total_marks int)"
#cursor.execute(sql)
#connection.commit()
#print("table created successfully")
sql2 ="insert into practice values(103,'anuj mehera', 11, 85)"
cursor.execute(sql2)
connection.commit()
print("data inserted successfully")
sql3 = "select * from practice"
cursor.execute(sql3)
result = cursor.fetchall()
connection.close()
print(result)