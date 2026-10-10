a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if(a>=b and a>=c):
    print(a,"is largest num")
elif(b>=a and b>=c):
    print(b,"is largest num")
else:
    print(c,"is largest num")
