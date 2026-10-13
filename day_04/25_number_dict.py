n=int(input("enter n:"))
dict={}
for i in range(1,n+1):
    dict[i]=i**2
print(dict)

#or 

dict={i:i**3 for i in range(1,n+1)}
print(dict)