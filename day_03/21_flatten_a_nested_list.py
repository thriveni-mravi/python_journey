nested_list=[[2,4,6],[3,6,9],[4,8,12]]
list1=[]
i=0
while i < len(nested_list):
    j=0
    while j < len(nested_list[i]):
        list1.append(nested_list[i][j])
        j+=1
    i+=1
print(list1)

#or

list=[]
for i in nested_list:
    list+=i
print(list)