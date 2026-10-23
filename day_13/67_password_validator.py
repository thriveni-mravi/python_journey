password=input("enter password:")
if len(password)>=8:
    if not password.isalnum() and any(i.isupper() for i in password) and any(i.islower() for i in password )and any(i.isdigit() for i in password):
        if " " not in password:
            print("Strong password")
        else:
            print("space is not allowed in password")
    else:
        print("password must consist of atleast 1 number,1uppercase and 1 lowercase latters and 1 symbol") 
else:
    print("password mush contains atleast 8 character")