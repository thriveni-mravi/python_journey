class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def show_student_details(self):
        print("name=",self.name)
        print("marks=",self.__marks)
Student=student("thriveni",90)
Student.show_student_details()