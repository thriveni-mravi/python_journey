try:
    digit=input("enter multidigit number:")
    if not digit.isdigit():
        print("enter positive integer value")
        
    sum1=0
    for i in digit:
        sum1+=int(i)

    print("sum of digits is",sum1)

    reverse_digit=digit[::-1]
    print("reverse of digit is",reverse_digit)

    if digit==digit[::-1]:
        print("the number is palindrome")
    else:
        print("the number is not a palindrom")

    sum2=0
    for i in digit:
        sum2+=(int(i)**len(digit))
    if sum2==int(digit):
        print("it is a armstrong number")
    else:
        print("not a armstrong number")

except ValueError:
    print("enter integer value only")
except Exception as e:
    print(e)


              




