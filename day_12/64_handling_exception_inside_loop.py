n=[]
for i in range(5):
    try:
        k=int(input(f"value{i+1}:"))
        n.append(k)
    except ValueError :
        print("invalid input try again")
        k=int(input(f"value{i+1}:"))
        n.append(k)
print("sum of 5 values is",sum(n))

