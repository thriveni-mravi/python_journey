class counter:
    def __init__(self,value):
        self.value=value
    def increment(self):
        self.value+=1
        return self.value
    def decrement(self):
        self.value-=1
        return self.value
    def display(self):
        return self.value

value=int(input("enter value:"))
Counter=counter(value)
print("incremented value:",Counter.increment(),"\ndecremented value:",Counter.decrement(),"\ndisplay value:",Counter.display())