def fact(n):
    if n<=1:
        return 1
    else:
        factorial=n*fact(n-1)
        return factorial
n=int(input("enter num:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=fact(digit)
    temp//=10
print(sum==n)
