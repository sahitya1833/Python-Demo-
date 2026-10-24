import pymysql

def test_deletea_01():
    connection = pymysql.connect(host = 'localhost', port =3306, user ='root',password='root', db ="corepython")
    cursor = connection.cursor()
    sql = "delete from marksheet where id = 21"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("data delete successfully")


def test_delete_02():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="corepython")
    cursor = connection.cursor()
    sql ="delete from marksheet where id =%s"
    data = 20
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data delete successfully")


def test_delete_03(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="corepython")
    cursor = connection.cursor()
    sql ="delete from marksheet where id =%s"
    data =id
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data delete successfully")


test_deletea_01()
test_delete_02()
test_delete_03(19)



