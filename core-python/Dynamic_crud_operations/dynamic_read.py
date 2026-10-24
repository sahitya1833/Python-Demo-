import pymysql

def test_read_01():
    connection = pymysql.connect(host='localhost', port=3306, user='root',password='root', database='corepython')
    cursor = connection.cursor()
    sql= "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    for i in result:
        print(i)
    connection.close()

def test_read_03():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='corepython')
    cursor = connection.cursor()
    sql ="select * from marksheet"
    #sql ="select * from marksheet where id = 1"
    #sql = "select * from marksheet where roll_no = 101"
    #sql = "select * from marksheet where name ='anuj' "
    #sql = "select * from marksheet where physics = 77"
    #sql = "select * from marksheet where chemistry = 80"
    #sql = "select * from marksheet where maths = 90"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    for i in result:
        print (i)
    connection.close()


def test_read_5(data={}):
    id = data.get('id',0)
    roll_no = data.get('roll_no',0)
    name = data.get('name',' ')
    physics = data.get('physics',0)
    chemistry =data.get('chemistry',0)
    maths =data.get('maths',0)
    pageno = data.get('pageNo', 0)
    pagesize = data.get('pageSize', 0)
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='corepython')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id !=0:
        sql+=" and id=" + str(id)
    if roll_no!=0:
        sql+=" and roll_no ="+ str(roll_no)
    if name!=' ':
        sql+=" and  name like '" + name +"%'"
    if physics !=0:
        sql+=" and physics=" + str(physics)
    if chemistry !=0:
        sql+=" and chemistry=" + str(chemistry)
    if maths !=0:
        sql+=" and maths=" + str(maths)
    if pagesize > 0:
        pageno = (pageno - 1) * pagesize
        sql += " limit " + str(pageno) + ", " + str(pagesize)

    print("sql:-",sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(result)

    connection.commit()
    connection.close()


data ={}
#data['id'] =18
#data['roll_no']=444
data['name'] ="s"
#data['physics']= 77
#data['chemistry']=80
#data['maths']=90

test_read_5(data)









