str="hrjhjkkjghjhghjr"
for i in str:
    if str.count(i)==1:
        print("first non repeating character in",str,"is",i)
        break
else:
    print("no non repeating char in",str)
