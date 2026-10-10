num=int(input("enter multidigit number:"))
n=0
while num>0:
    digit=num%10
    n+=digit
    num//=10
print("sum of digits is",n)