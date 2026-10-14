a,b=map(int,input("enter 2 numbers:").split())
small_num=min(a,b)
for i in range(2,small_num):
    if a%i==0 and b%i==0:
        print(f"gcd({a},{b}) is {i}")
        break


#or 
while b!=0:
    a,b=b,a%b
print("gcd:",a)