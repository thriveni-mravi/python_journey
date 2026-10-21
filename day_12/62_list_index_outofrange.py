num=[2,4,6,8,10]
try:
    index=int(input("enter index :"))
    print(num[index])
except IndexError as e:
    print(e)
