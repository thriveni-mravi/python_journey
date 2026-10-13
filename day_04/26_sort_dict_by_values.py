dict1={"pen":5,"pencil":25,"book":16,"sharpner":3}
print(dict(sorted(dict1.items(),key=lambda dict1:dict1[1])))