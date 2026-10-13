n=int(input("enter num:"))
if n<2:
    print(n,"is not prime num")
else:
    for i in range(2,n):
        if (n%i==0):
            print(n,"is not prime num")
            break
    else:
        print(n,"is prime num")

#or

n2=int(input("enter num2:"))
if n<2:
    print(n,"is not prime num")
else:
    for i in range(2,int(n2**0.5)+1):
        if (n2%i==0):
            print(n2,"is not prime num")
            break
    else:
        print(n2,"is prime num")