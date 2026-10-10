a=int(input("enter a:"))
b=int(input("enter b:"))
print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.floor division\n6.modulus\n7.exponent\n")
choice=int(input("enter choice:"))
match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        if(b==0):
            print("division by zero is not allowed")
        else:
            print(float(a/b))
    case 5:
        if(b==0):
            print("division by zero is not allowed")
        else:
            print(float(a//b))
    case 6:
        if(b==0):
            print("division by zero is not allowed")
        else:
            print(float(a%b))
    case 7:
        print(a**b)


