text=input("enter sentance:")
words_count=1  # 1 because the program doesn't count the last word
for i in text:
    if i==" ":
        words_count+=1
print("num of words in given text is",words_count)

#or

text2=input("enter sentance 2:")
text2=text2.split()
print("num of words in given text is",len(text2))
