str1=input("str1=").replace(" ","").lower()
str2=input("str2=").replace(" ","").lower()
anagram=True
if len(str1)==len(str2):

    for ch1 in str1:
        if str1.count(ch1)!=str2.count(ch1):
            anagram=False
            break
if anagram==True:
    print(str1,"&",str2,"are anagram words")
else:
     print(str1,"&",str2,"are not anagram words")

#or


str3=input("str3=").replace(" ","").lower()
str4=input("str4=").replace(" ","").lower()
if sorted(str3)==sorted(str4):
    print(str3,"&",str4,"are anagram words")
else:
    print(str3,"&",str4,"are not anagram words")


