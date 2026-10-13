str="hello everyone ,I started to learn and practice python".split()
dict1={}
for i in str:
    length=len(i)
    if length not in dict1:
        dict1[length]=[]
    dict1[length].append(i)
print(dict1)
