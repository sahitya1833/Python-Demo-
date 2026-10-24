class Shape:
    def __init__(self):
        self.color =''
        self.border_width=0

    def set_color(self,color):
        self.color = color

    def get_color(self):
        return self.color

    def set_border_width(self,border):
        self.border_width= border

    def get_border_width(self):
        return self.border_width

class Rectangle(Shape):
    def  __init__(self):
        self.length =0
        self.width = 0

    def set_length(self,length):
        self.length =length

    def get_length(self):
        return self.length

    def set_width(self,width):
        self.width=width

    def get_width(self):
        return self.width

class Circle(Shape):
    def __init__(self):
        self.radius=0

    def set_radius(self,radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
r = Rectangle()
r.set_length(20)
r.set_color('green')
r.set_border_width(50)
r.set_width(10)
print("RECTANGLE")
print("color of the rectangle is:",r.get_color())
print("length of the rectangle is:",r.get_length())
print("width of the rectangle is:",r.get_width())
print("border of the rectangle is:",r.get_border_width())


c = Circle()
c.set_radius(5)
c.set_color('red')
c.set_border_width(18)
print("CIRCLE")
print("color of the circle is:",c.get_color())
print("radius of the circle is:",c.get_radius())
print("border of the circle is:",c.get_border_width())




