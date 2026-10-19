class Student:
    college_name="XYZ"  
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)
        print("college name:",Student.college_name)

n=int(input("enter num of student:"))
students=[]
for i in range(n):
    name=input("enter name:")
    marks=float(input("enter marks:"))
    student=Student(name,marks)
    students.append(student)

print("student deytails:")
for student in students:
    student.display()
    print()
    
