
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def circumferance(self):
        return 2*3.14*self.radius
radius=float(input("enter radius:"))
Circle=circle(radius)
print("area:",Circle.area())
print("circumference:{:.2f}".format(Circle.circumferance()))
