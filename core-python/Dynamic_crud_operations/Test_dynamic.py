from os import close

import pymysql


def test_insert(data={}):
    id = data.get('id')
    name = data.get('name')
    description = data.get('description')
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='corepython')
    cursor = connection.cursor()
    sql = "insert into roll values(%s, %s, %s)"
    data = (id, name, description)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


# data ={}
# data['id']= 6
# data['name']= 'marketing'
# data['description']= "executive"

# test_insert(data)

# UPDATE
def test_update(data2={}):
    id = data2.get('id')
    name = data2.get('name')
    description = data2.get('description')
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="corepython")
    cursor = connection.cursor()
    sql = "update roll set name=%s, description=%s where id=%s"
    data = (name, description, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


# data2={}
# data2['id']=1
# data2['name']='marketing'
# data2['description']="executive"

# test_update(data2)


# DELETE
def test_delete(id):
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="corepython")
    cursor = connection.cursor()
    sql = "delete from roll where id =%s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("record delete successfully")


# test_delete(5)


# READ
def test_read(data={}):
    id = data.get('id', 0)
    name = data.get('name', ' ')
    description = data.get('description', ' ')
    page_no = data.get('page_no', 0)
    page_size = data.get('page_size', 0)
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="corepython")
    cursor = connection.cursor()
    sql = "select * from roll where 1=1"
    if id != 0:
        sql += ' and id = ' + str(id)
    if name != ' ':
        sql += " and name like '" + name + "%'"
    if description != ' ':
        sql += " and description '" + description + "%'"

    if page_size > 0:
        page_no = (page_no - 1) * page_size
        sql += " limit " + str(page_no) + ", " + str(page_size)

    print('sql =>', sql)
    cursor.execute(sql)
    connection.commit()
    connection.close()


data = {}
# data['id'] = 1
# data['name']="sales role"
test_read(data)
