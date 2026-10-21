try:
    n=int(input("enter num of student:"))
    for i in range(n):
        name=input("enter name:")
        marks=float(input("enter marks:"))
        if marks<0 or marks>100:
            raise ValueError ("invalid marks,marks must between 0 and 100")
        print(name," marks:",marks)
except ValueError as e:
    print(e)
