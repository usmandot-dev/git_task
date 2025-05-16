# book_library.py (Refactored for GUI - Reusing from Tkinter)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class BookNotAvailableError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return book
        raise BookNotAvailableError("Book is not available.")

    def return_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def books_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]
