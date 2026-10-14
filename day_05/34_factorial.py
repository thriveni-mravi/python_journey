def fact(n):
    if n<=1:
        return 1
    else:
        fact1=n*fact(n-1)
        return fact1
n=int(input("enter num:"))
print(fact(n))