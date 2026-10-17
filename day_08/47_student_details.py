class student:
    def __init__(self,name,usn,branch):
        self.name=name
        self.usn=usn
        self.branch=branch
    def __str__(self):
        return f"student details \n name:{self.name} \n usn:{self.usn}\n branch:{self.branch}"
std1=student("thriveni","4xyz5mno6","CSE")
print(std1)