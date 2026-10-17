class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def __str__(self):
        return f"area of rectangle={self.breadth*self.length} \nperimeter of rectangle={2*(self.breadth+self.length)}"
length=int(input("enter lengthy of rectangle:"))
breadth=int(input("enter breadth of rectangle:"))
rect=rectangle(length,breadth)
print(rect)
    