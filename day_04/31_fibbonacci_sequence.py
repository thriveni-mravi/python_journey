def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        res=fib(n-1)+fib(n-2)
        return res

n=int(input("enter num:"))
print(fib(n))

