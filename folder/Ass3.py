import datetime
import random
import time
import threading
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.__copies = 0
        self.added_date =datetime.date.today()
        self.book_id = random.randint(100,999)

    def display(self):
        print("Book Title:",self.title)
        print("Book Author:",self.author)
        print("Book copy:",self.get_copies())
        print("Book Added_date:",self.added_date)
        print("Book id:",self.book_id)
        print("--------------")
        

    def get_copies(self):
        return self.__copies

    def add_copies(self,count):
        if count <=0:
            raise ValueError("add_copies cannot be negative")
        self.__copies = self.__copies + count


    def borrow_copies(self):

        if self.__copies <=0:
            raise ValueError("Book is not available")
        self.__copies -=1
        print("Book left after borrow:",self.__copies)
        print("Book Borrow Succesfully")

class Library:
    def __init__(self,library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def show_all(self):
        for book in self.books:
            book.display()
            print("--------")
    
class Ebook(Book):
    def __init__(self,title,author,file_format):
        super().__init__(title,author)
        self.file_format = file_format

    def download(self):
        print(f"Downloading{self.title} in {self.file_format} format")

    def display(self):
        super().display()
        print("File Format:",self.file_format)

def sync_catalog(book):
    print("Syncing catalog...")
    time.sleep(2)
    book.display()
    



b1 = Book("Mathematics Algebra","RD SHARMA")
b2 = Ebook("Mathematics Algebra","RD SHARMA","PNG")
b1.add_copies(4)
try:
    b1.borrow_copies()

except ValueError as e:
    print("Error:",e)

t1 = threading.Thread(target=sync_catalog,args=(b1,))
t1.start()
t1.join()



