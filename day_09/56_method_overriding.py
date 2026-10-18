class shape:
    def area(self):
        return " area is not defined"
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return f"area of rectangle:{self.length*self.breadth}"
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"area of circle:{3.14*self.radius**2}"

Rectangle=rectangle(5,10)
Circle=circle(5)
print(Rectangle.area())
print(Circle.area())
        