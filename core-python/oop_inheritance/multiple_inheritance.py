class Addition:
    def sum(self,a,b):
        return a+b

class Multiplication:
    def multiply(self,a,b):
        return a*b


class Devision:
    def divide(self,a,b):
        return a/b

class test(Addition,Multiplication,Devision):
    pass

t = test()
print(t.sum(20,30))
print(t.divide(100,20))
print(t.multiply(18,21))






