import tkinter as tk
from tkinter import messagebox, simpledialog

# ====== Class Definitions ======

class BookNotAvailableError(Exception):
    pass

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
        self.lent_books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.lent_books.append(book)
        else:
            raise BookNotAvailableError("This book is not available to lend.")

    def return_book(self, book):
        if book in self.lent_books:
            self.lent_books.remove(book)
            self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def __iter__(self):
        return iter(self.books)

    def books_by_author(self, author_name):
        return [book for book in self.books if book.author == author_name]

class DigitalLibrary(Library):
    def __init__(self):
        super().__init__()
        self.ebooks = []

    def add_ebook(self, book, size_in_mb):
        self.ebooks.append((book, size_in_mb))

# ====== GUI Starts Here ======

library = DigitalLibrary()

def toggle_ebook_entry():
    if is_ebook.get():
        entry_size.config(state='normal')
    else:
        entry_size.config(state='disabled')
        entry_size.delete(0, tk.END)

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    isbn = entry_isbn.get()

    if not title or not author or not isbn:
        messagebox.showwarning("Input Error", "Please fill all required fields.")
        return

    book = Book(title, author, isbn)
    library.add_book(book)

    if is_ebook.get():
        try:
            size = float(entry_size.get())
            library.add_ebook(book, size)
        except ValueError:
            messagebox.showerror("Invalid Size", "Please enter a valid eBook size.")
            return

    messagebox.showinfo("Success", "Book added successfully!")
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)
    entry_size.delete(0, tk.END)
    toggle_ebook_entry()
    update_listbox()

def lend_book():
    selected = listbox_books.curselection()
    if not selected:
        messagebox.showinfo("Select Book", "Select a book to lend.")
        return
    book_str = listbox_books.get(selected)
    book = get_book_from_string(book_str)
    try:
        library.lend_book(book)
        messagebox.showinfo("Lent", f"You lent: {book}")
        update_listbox()
    except BookNotAvailableError as e:
        messagebox.showerror("Unavailable", str(e))

def return_book():
    title = simpledialog.askstring("Return Book", "Enter book title to return:")
    if title:
        for b in library.lent_books:
            if b.title == title:
                library.return_book(b)
                messagebox.showinfo("Returned", f"Returned: {b}")
                update_listbox()
                return
        messagebox.showerror("Not Found", "Book not found in lent list.")

def remove_book():
    selected = listbox_books.curselection()
    if not selected:
        messagebox.showinfo("Select Book", "Select a book to remove.")
        return
    book_str = listbox_books.get(selected)
    book = get_book_from_string(book_str)
    library.remove_book(book)
    messagebox.showinfo("Removed", f"Removed: {book}")
    update_listbox()

def view_by_author():
    author = simpledialog.askstring("Search Author", "Enter author's name:")
    if author:
        books = library.books_by_author(author)
        if books:
            books_text = "\n".join(str(b) for b in books)
            messagebox.showinfo("Books by Author", books_text)
        else:
            messagebox.showinfo("No Books", "No books by this author.")

def update_listbox():
    listbox_books.delete(0, tk.END)
    for book in library:
        listbox_books.insert(tk.END, str(book))

def get_book_from_string(book_str):
    for book in library:
        if str(book) == book_str:
            return book
    return None

# ====== GUI Layout ======

window = tk.Tk()
window.title("Library Management System")
window.geometry("550x600")

frame = tk.Frame(window)
frame.pack(pady=10)

# Book input fields
tk.Label(frame, text="Title:").grid(row=0, column=0, sticky='e')
entry_title = tk.Entry(frame, width=30)
entry_title.grid(row=0, column=1)

tk.Label(frame, text="Author:").grid(row=1, column=0, sticky='e')
entry_author = tk.Entry(frame, width=30)
entry_author.grid(row=1, column=1)

tk.Label(frame, text="ISBN:").grid(row=2, column=0, sticky='e')
entry_isbn = tk.Entry(frame, width=30)
entry_isbn.grid(row=2, column=1)

# eBook Checkbox and size input
is_ebook = tk.BooleanVar()
ebook_check = tk.Checkbutton(frame, text="Is eBook?", variable=is_ebook, command=toggle_ebook_entry)
ebook_check.grid(row=3, column=0, sticky='e')

entry_size = tk.Entry(frame, width=30, state='disabled')
entry_size.grid(row=3, column=1)
tk.Label(frame, text="Size in MB").grid(row=3, column=2)

# Buttons
btn_add = tk.Button(window, text="Add Book", width=20, command=add_book)
btn_add.pack(pady=5)

btn_lend = tk.Button(window, text="Lend Book", width=20, command=lend_book)
btn_lend.pack(pady=5)

btn_return = tk.Button(window, text="Return Book", width=20, command=return_book)
btn_return.pack(pady=5)

btn_remove = tk.Button(window, text="Remove Book", width=20, command=remove_book)
btn_remove.pack(pady=5)

btn_author = tk.Button(window, text="View Books by Author", width=20, command=view_by_author)
btn_author.pack(pady=5)

# Display Listbox
tk.Label(window, text="Available Books:").pack()
listbox_books = tk.Listbox(window, width=60)
listbox_books.pack(pady=10)

update_listbox()
window.mainloop()