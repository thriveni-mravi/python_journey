str=input("enter string value:").lower()
if str==str[::-1]:
    print(str,"is palindrome")
else:
    print(str,"is not palindrom")