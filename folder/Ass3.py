import datetime
import random
import time
import threading
import asyncio

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
            raise outofstock(f"{self.title} book out of stock")
        self.__copies -=1
        print("Book left after borrow:",self.__copies)
        print("Book Borrow Succesfully")

    async def synccatalog(self):
        print(f"Syncing {self.title}....")
        await asyncio.sleep(2)
        print(f"Sync complete for {self.title}...")

    def backup_book(self):
        print(f"Backing up {self.title}...")
        time.sleep(2)
        print(f"Backup finished for {self.title}")

    def start_backup(self):
        t = threading.Thread(target=self.backup_book)
        t.start()
        t.join()
class Library:
    branch = "kotrud"
    def __init__(self,library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def show_all(self):
        for book in self.books:
            book.display()
            print("--------")

    @classmethod
    def change_branch(cls,branch):
        cls.branch = branch
    
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


class outofstock(Exception):
    pass
    

b1 = Book("Mathematics Algebra","RD SHARMA")
b2 = Ebook("Mathematics Algebra","RD SHARMA","PNG")
asyncio.run(b1.synccatalog())

b1.add_copies(4)
b1.start_backup()
try:
    b1.borrow_copies()

except outofstock as e:
    print("Error:",e)






