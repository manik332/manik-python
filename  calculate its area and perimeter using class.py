class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print(3.14*self.radius**2)
    
    def perimeter(self):
        print(2*3.14*self.radius)

cir=circle(6)
cir.area()
cir.perimeter()