from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QListWidget, QMessageBox
import sys

# Your book classes (same as before)
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class DigitalLibrary(Library):
    def __init__(self):
        super().__init__()
        self.ebooks = []

    def add_ebook(self, book, size):
        self.ebooks.append((book, size))

class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library GUI (PyQt5)")
        self.resize(400, 500)

        self.library = DigitalLibrary()

        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.isbn_input = QLineEdit()
        self.size_input = QLineEdit()
        self.size_input.setEnabled(False)

        self.checkbox = QCheckBox("Is eBook?")
        self.checkbox.stateChanged.connect(self.toggle_ebook)

        self.add_button = QPushButton("Add Book")
        self.add_button.clicked.connect(self.add_book)

        self.book_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Author:"))
        layout.addWidget(self.author_input)
        layout.addWidget(QLabel("ISBN:"))
        layout.addWidget(self.isbn_input)
        layout.addWidget(self.checkbox)
        layout.addWidget(QLabel("eBook Size (MB):"))
        layout.addWidget(self.size_input)
        layout.addWidget(self.add_button)
        layout.addWidget(QLabel("Books in Library:"))
        layout.addWidget(self.book_list)

        self.setLayout(layout)

    def toggle_ebook(self):
        self.size_input.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.size_input.clear()

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        isbn = self.isbn_input.text()

        if not title or not author or not isbn:
            QMessageBox.warning(self, "Input Error", "Fill all fields.")
            return

        book = Book(title, author, isbn)
        self.library.add_book(book)

        if self.checkbox.isChecked():
            try:
                size = float(self.size_input.text())
                self.library.add_ebook(book, size)
            except ValueError:
                QMessageBox.warning(self, "Input Error", "Enter valid eBook size.")
                return

        self.book_list.addItem(str(book))
        self.title_input.clear()
        self.author_input.clear()
        self.isbn_input.clear()
        self.size_input.clear()
        self.checkbox.setChecked(False)

app = QApplication(sys.argv)
window = LibraryApp()
window.show()
sys.exit(app.exec_())
