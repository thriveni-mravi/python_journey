str=input("enter string value:")
str2=""
for ch in str:
    if ch not in str2:
        str2+=ch
        count=str.count(ch)
        print(ch,"=",count)


