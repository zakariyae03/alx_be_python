# library_system.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

class PrintBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}, {self.pages} pages"

class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}, {self.file_size}MB"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

# Testing the classes in main.py

from library_system import Book, PrintBook, EBook, Library

def main():
    # Create instances of books
    book1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 277)
    book2 = EBook("1984", "George Orwell", 1949, 1.2)
    book3 = PrintBook("To Kill a Mockingbird", "Harper Lee", 1960, 281)

    # Create a library and add books to it
    my_library = Library()
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
