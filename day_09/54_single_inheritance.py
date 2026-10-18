class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class student(Person):
    def __init__(self,name,age,usn,branch):
        super().__init__(name,age)
        self.usn=usn
        self.branch=branch
    def display(self):
        return f"name:{self.name}\n age:{self.age}\n usn:{self.usn}\n branch:{self.branch}"
    
name=input("enter name:")
age=int(input("enter age:"))
usn=input("enter usn:")
branch=input("enter branch:")

std_details=student(name,age,usn,branch)
print("display the student details:\n",std_details.display())