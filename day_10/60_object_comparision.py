class Student: 
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)

n=int(input("enter num of student:"))
students=[]
for i in range(n):
    name=input("enter name:")
    marks=float(input("enter marks:"))
    student=Student(name,marks)
    students.append(student)

highest_marks=students[0]
for student in students:
    if student.marks>highest_marks.marks:
        highest_marks=student
print("student with highest marks:")
highest_marks.display()
