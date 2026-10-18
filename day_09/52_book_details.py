class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        return f"Book details are\nTitle:{self.title}\nauthor:{self.author}\nprice:{self.price}"

    
title=input("enter book title:")
author=input("enter author name:")
price=float(input("enter price:"))

book=Book(title,author,price)
print(book.display())
