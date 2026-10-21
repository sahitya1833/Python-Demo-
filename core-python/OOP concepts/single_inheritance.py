class Shape:
    def __int__(self):
        self.color=''
        self.border_width=0

    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color

    def set_border_width(self,bw):
        self.border_width= bw

    def get_border_width(self):
        return self.border_width

class Rectangle(Shape):
    def __int__(self):
        self.length=0
        self.width=0

    def set_length(self,length):
        self.length = length
    def get_length(self):
        return self.length

    def set_width(self,width):
        self.width=width
    def get_width(self):
        return self.width

r = Rectangle()
r.set_color('red')
r.set_border_width(30)
r.set_length(22)
r.set_width(11)

print("color of the rectangle are..", r.get_color())
print("border of the rectangle are..",r.get_border_width())
print("length of the rectangle are..",r.get_length())
print("width of the rectangle are..",r.get_width())













