class person():

    def __init__(self):   #calling constructor
        print("calling constructor...")
        self.name = ""          #adding attribute1
        self.DOB = ""           #adding attribute2
        self.address = ""       #adding attribute3


    def setName(self, name):        #allocating a memory to Name
        print("calling set name")
        self.name = name
        print("name has been added successfully...")

    def getName(self):              #retriving name
        print("calling Get Name")
        return self.name

    def setDOB(self,dob):
        print("calling set DOB...")
        self.DOB= dob
        print("DOB has been added successfully...")
    def getDOB(self):
        print("calling get DOB...")
        return self.DOB

    def setAddress(self,address):
        print("calling set Address...")
        self.address = address
        print("Address has been added successfully...")
    def getAddress(self):
        print("calling get address...")
        return self.address

p = person()
p.setName("sahitya")
print(p.getName())
p.setDOB("18-03-2004")
print(p.getDOB())
p.setAddress("satyam palace indore")
print(p.getAddress())
