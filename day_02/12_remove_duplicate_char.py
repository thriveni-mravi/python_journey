str=input("enter string value:")
str2=""
for i in str:
    if i not in str2:
        str2+=i
print(str," after removing duplicate characters:",str2)

