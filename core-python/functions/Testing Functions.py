#calling a function
def welcome():
    print("welcome to the python world")
welcome()


#function with parameters
def greet(name):
    print("hello", name)
greet('sahitya')
greet("pranjay")


#positional arguments
def students(name,city):
    print(name,"lives in city",city)
students("sahitya","indore")


#keywords arguments
def movie(name,rating):
    print(name,"rating is",rating)
movie(rating=10, name= "sahitya")


#defaults arguments
def studnet(name, city="indore"):
    print(name,"lives in city",city)
studnet("sahitya")
studnet("pranjay","pachmarhi")


# *args - Unlimited input
def total_marks(*marks):
    print(marks)
total_marks(10,30,40,55,99,100)


#**kwargs - Named Unlimited Inputs
def student_info(**data):
    print(data)
student_info(name='sahitya', city= "indore",work= "studnet")


#return statement
def add(a,b):
    return a+b
result = add(10,20)
print (result)


#multiple return values
def student():
    return "sahitya", 22, "indore"
name,age,city = student()
print(name)
print(age)
print(city)



