class Publisher:
    def __init__(self, name):
        self.name = name

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Publisher: {self.name}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display_info(self):  
        super().display_info()
        print(f"Price: ${self.price}")
        print(f"No. of Pages: {self.no_of_pages}")


publisher_name = input("Enter Publisher's name: ")
book_title = input("Enter Book's title: ")
book_author = input("Enter Book's author: ")
python_price = float(input("Enter Python book's price: "))
python_pages = int(input("Enter Python book's number of pages: "))

python_book = Python(publisher_name, book_title, book_author, python_price, python_pages)

python_book.display_info()

