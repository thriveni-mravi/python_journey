while True:
    try:
        a=int(input("enter a:"))
        b=int(input("enter b:"))
        print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.floor division\n6.modulus\n7.exponent\n")
        choice=int(input("enter choice:"))
        match choice:
            case 1:
                print("result:",a+b)
            case 2:
                print("result:",a-b)
            case 3:
                print("result:",a*b)
            case 4:
                if(b==0):
                    print("division by zero is not allowed")
                else:
                    print("result:",float(a/b))
            case 5:
                if(b==0):
                    print("division by zero is not allowed")
                else:
                    print("result:",float(a//b))
            case 6:
                if(b==0):
                    print("division by zero is not allowed")
                else:
                    print("result:",float(a%b))
            case 7:
                print("result:",a**b)
            case _:
                print("choice must be greater than 0 and less than 8\n")
        user_wish=int(input("do u want to continue calculation:\nfor yes print 1 \nfor no print 0\ncontinue?="))
        
        while user_wish not in (0,1):
            user_wish=int(input("enter 1 or 0:"))

        if user_wish ==0:
            break
            
               
    except ValueError as e:
        print("value error:",e)

print("------Calculation Completed!-------")
        


