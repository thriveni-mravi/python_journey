list1=[1,2,3,0,3,0,5,8,0,44,5,0]
for i in list1:
    if i==0:
        list1.remove(i)
        list1.append(i)
print(list1)
    



