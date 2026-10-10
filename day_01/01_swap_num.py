a=int(input("enter a:"))
b=int(input("enter b:"))
print("value of a and b before swapping:",a," ",b)
a,b=b,a   
# without third variable
print("\n value of a and b after swapping:",a," ",b)
#with third variable
temp=a
a=b
b=temp
print("\n value of a and b after swapping:",a," ",b)