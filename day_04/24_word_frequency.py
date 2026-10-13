sen=input("enter sentance:").split()
dict={}
for i in sen:
    if i not in dict:
        dict[i]=sen.count(i)
print(dict)

#or

for key in dict:
    print(key,"-",dict[key])
