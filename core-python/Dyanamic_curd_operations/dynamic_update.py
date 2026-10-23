import pymysql

def test_update_01():
    connection = pymysql.connect(host ='localhost' ,port=3306, user='root', password ='root',db='corepython' )
    cursor =connection.cursor()
    sql = "update marksheet set roll_no =111, name ='bhanu', physics =44, chemistry=55, maths = 33 where id =16"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("record update successfully")


def test_update_02():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='corepython')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no =%s, name =%s, physics =%s, chemistry=%s, maths =%s where id =%s"
    data = (222,'rishita',45,85,27,17)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("record updated successfully")


def test_update_03(roll_no,name,physics,chemistry,maths,id):

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='corepython')
    cursor = connection.cursor()
    sql= "update marksheet set roll_no =%s, name =%s, physics =%s, chemistry= %s, maths= %s where id= %s"
    data =(roll_no,name,physics,chemistry,maths,id)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("record updated successfully")


def test_update_04(data={}):
    id = data['id']
    roll_no = data['roll_no']
    name =data['name']
    physics= data['physics']
    chemistry=data['chemistry']
    maths=data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='corepython')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no =%s, name =%s, physics =%s, chemistry= %s, maths= %s where id= %s"
    data = (roll_no, name, physics, chemistry, maths, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("record updated successfully")


#test_update_01()
#test_update_02()
#test_update_03(333,"deepak", 55,60,33,10)

data= {}
data["id"]= 18
data['roll_no']= 444
data['name']= 'shiv'
data['physics']=77
data['chemistry']=80
data['maths']=90

test_update_04(data)









