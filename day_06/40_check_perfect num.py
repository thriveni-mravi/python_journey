def perfect_num(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    return sum==n
n=int(input("enter num:"))
print(perfect_num(n))


