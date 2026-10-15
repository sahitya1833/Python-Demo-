class Person:

    def __init__(self):   #calling constructor
        print("calling constructor...")
        self.name = ""          #adding attribute1
        self.DOB = ""           #adding attribute2
        self.address = ""       #adding attribute3


    def setname(self, name):        #allocating a memory to Name
        print("calling set name")
        self.name = name
        print("name has been added successfully...")

    def getname(self):              #retriving name
        print("calling Get Name")
        return self.name

    def setdob(self,dob):
        print("calling set DOB...")
        self.DOB= dob
        print("DOB has been added successfully...")
    def getdob(self):
        print("calling get DOB...")
        return self.DOB

    def setaddress(self,address):
        print("calling set Address...")
        self.address = address
        print("Address has been added successfully...")
    def getaddress(self):
        print("calling get address...")
        return self.address

p = Person()
p.setname("sahitya")
print(p.getname())
p.setdob("18-03-2004")
print(p.getdob())
p.setaddress("satyam palace indore")
print(p.getaddress())
