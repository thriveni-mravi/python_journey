a,b=map(int,input("enter 2 numbers").split())
count1=0
count2=0
for i in range(1,a//2+1):
    if a%i==0:
        count1+=i
for i in range(1,b//2+1):
    if b%i==0:
        count2+=i
print(count1==b and count2==a)
    