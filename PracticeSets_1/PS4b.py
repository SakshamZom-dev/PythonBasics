# Build a mini Library system

# Class: Book
#   attributes: title, author, __available (private, default True)
#   methods:
#     - info() → "Title: X | Author: Y"
#     - borrow() → if available, set to False, print "Borrowed"
#                  else print "Not available"
#     - return_book() → set available back to True, print "Returned"

class Book:

    def __init__(self, title, author):
        self.title  = title
        self.author = author
        self.__available = True

    def info(self):
        print(f"Title: {self.title} | Author: {self.author}")
    
    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"{self.title} Borrowed successfully")
        else:
            print("Can't Borrow, the book is not available")
    
    def return_book(self):
        self.__available = True
        print(f"{self.title} Returned successfully")        

# Create 2 books

b1 = Book("Harry Potter - Goblett of Fire", "J.K. Rowling")
b2 = Book("Marvel Spiderman Origins", "Stan Lee")

# Borrow one, try borrowing it again (should say not available)

b1.borrow()
b1. borrow()

# Return it, borrow again (should work now)

b1.return_book()
b1.borrow()

b2.borrow()