class Cars:
    def init(self):
        self.color=''
        self.model=''
        self.type=''

    def get_details(self):
        print("color", self.color)
        print("model", self.model)
        print("type", self.type )

c1 = Cars()
c1.color = "black"
c1.model ="suv"
c1.type = "petrol"
c1.get_details()


