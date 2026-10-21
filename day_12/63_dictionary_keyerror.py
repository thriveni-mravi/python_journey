try:
    n=int(input("enter num of students:"))
    students={}
    for i in range(n):
        name=input("name:")
        marks=float(input("marks:"))
        students[name]=marks

    name=input("enter name : ")
    print(f"{name} scored {students[name]} marks")
except KeyError :
    print("student not found")
except Exception as e:
    print(e)
finally:
    print("Thank you")

