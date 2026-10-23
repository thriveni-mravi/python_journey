n=int(input("enter number of subjects:"))
sub_dict={}
for i in range(n):
    sub=input("enter sub:")
    marks=float(input("enter marks:"))
    if marks<0 or marks>100:
        print("invalid marks! try again")
        marks=float(input("enter marks:"))
        
    sub_dict[sub]=marks

total_marks=sum(sub_dict.values())
print("total marks=",total_marks)

average_marks=total_marks/n
print("average marks=",average_marks)

percentage=int((total_marks/(n*100))*100)
print("percentage=",percentage,"%")


if percentage>=90 and percentage<=100:
    print("Grade O")
elif percentage>=75 and percentage<90:
    print("Grade A")
elif percentage>=50 and percentage<75:
    print("Grade B")
elif percentage>=35 and percentage<50:
    print("Grade c")
else:
    print("Grade F")

highest_marks=max(sub_dict.values())
lowest_marks=min(sub_dict.values())

print("highest marks=",highest_marks)
print("lowest marks=",lowest_marks)





