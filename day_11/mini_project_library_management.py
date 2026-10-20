class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_available=True
    def borrow_book(self):
        if self.is_available==False:
            print("book is not available")
        else:
            print("book is available")
            print("book is borrowed")
            self.is_available=False
    def return_book(self):
        if self.is_available==False:
            print("book is returned successfully")
            self.is_available=True
        else:
            print("book is not returned ")
    def display(self):
        print("book title:",self.title)
        print(" author:",self.author)
        if self.is_available:
            print(" status:available")
        else:
            print("status:not available")
    def search(self):
        print("title:",self.title)
        print("author:",self.author)
n=int(input("enter number of books:"))
books=[]
for i in range(n):
    print(f"enter book {i+1} details ")
    title=input("title:")
    author=input("author:")
    book=Book(title,author)
    books.append(book)

print("=========LIBRARY MANAGEMENT MENU==========")
print("1.display all books")
print("2.borrow a book")
print("3.return a book")
print("4.search for a book")
print("5.exit")


while True: 
    choice=int(input("enter choice(1-5):"))
    match (choice):
        case 1:
            print("-----book details-----")
            for book in books:
                book.display()
                print("   ---------   ")
                
        case 2:
            title=input("enter the book title to borrow a book:")
            found=True
            for book in books:
                if book.title==title:
                    book.borrow_book()
                    found=True
                    break

                else:
                    found=False
            if not found:
                print("book is not found")

        case 3:
            title2=input("enter the book title to return a book:")
            for book in books:
                found=True
                if book.title==title2:
                    book.return_book()
                    found=True
                    break
                else:
                    found=False
            if not found:
                print("book is not found")  

        case 4:
            search_book=input("enter the book title for search: ")
            for book in books:
                found=True
                if book.title==search_book:
                    found=True
                    print("book is found")
                    book.search()
                    break
                else:
                    found=False
            if not found:
                print("book is not found")

        case 5:
            print("--------Exit---------")
            break

        case _:
            print("invalid choice")  
        

    



    

    

    