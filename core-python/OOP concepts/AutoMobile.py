class Automobile:
    no_of_gears =6
    def __int__(self):
        self.__color =''
        self.__brand =''
        self.__speed =0
    def set_color(self,color):
        self.__color = color
    def get_color(self):
        return self.__color

    def set_brand(self,brand):
        self.__brand = brand
    def get_brand(self):
        return self.__brand

    def set_speed(self,speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def accelerator(self):
        if self.__speed >= 400:
            print("Speed limit is high, please apply brake")
        else:
            self.__speed += 10
            print("Current speed:", self.__speed)


car =Automobile()
car.set_color("graphite grey")
car.set_speed(350)
car.set_brand("audi")

print(car.get_color())
print(car.get_speed())
print(car.get_brand())

car.accelerator()

