try:
    n=int(input("enter n:"))
    m=int(input("enter m:"))
    div=n/m
    print(div)
except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("invalid input")
    
finally:
    print("program runs successfully")

