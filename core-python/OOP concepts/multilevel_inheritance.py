class Student:
    def get_student(self):
        self.name = input("enter a name..")
        self.age = int(input("enter a age.."))
        self.gender = input("enter a gender..")


class Test(Student):
    def getmarks(self):
        self.student_class =int(input("class"))
        print("enter the marks of the respective class")
        self.maths =int(input("enter maths marks"))
        self.english =int(input ("enter english name"))
        self.hind = int(input("enter hindi marks"))
        self.physics =int(input("enter Physics marks"))

class Marks(Test):
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)
        print("class", self.student_class)
        print("mathe marks",self.maths)
        print("english marks",self.english)
        print("hindi marks",self.hind)
        print("physics marks",self.physics)
        total_marks = self.maths + self.physics +self.hind+ self.english
        if total_marks > 120:
            print("passed")
        else:
            print("failed")
        print("total marks:", total_marks)


m =Marks()
m.get_student()
m.getmarks()
m.display()





