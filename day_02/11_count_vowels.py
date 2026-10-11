str=input("enter a string value:")
vowels_count=0
for i in str:
    if i in "aeiouAEIOU":
        vowels_count+=1
print("number of vowels in",str,"is",vowels_count)
        
