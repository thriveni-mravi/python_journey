num=input("enter num:")
n=len(num)
total=0
for i in num:
    total+=(int(i)**n)
if total==int(num):
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")


