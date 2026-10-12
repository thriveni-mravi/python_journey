list1=[22,43,24,65,54,66,88,88,44,65,43,22]
for i in list1:
    if list1.count(i)>=2:
        list1.remove(i)
print(list1)

