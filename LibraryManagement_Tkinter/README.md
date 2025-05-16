# Library Management System (Tkinter)

## 📌 Project Overview

This is a GUI-based Library Management System built using **Tkinter** in Python. It allows users to add, lend, return, and remove books from the library. It also supports eBooks with download sizes.

## 🚀 Features

* Add, Lend, Return, and Remove Books.
* Support for both physical and eBooks.
* Custom error handling for unavailable books.
* eBook field is disabled until the checkbox is checked.
* Clean, user-friendly interface.

## 📂 Project Structure

```
├── book_library.py  # Core logic of the library
├── gui_app.py       # GUI interface using Tkinter
└── README.md        # Project instructions
```

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/LibraryManagement_Tkinter.git
cd LibraryManagement_Tkinter
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv_tkinter
source venv_tkinter/bin/activate  # For Mac/Linux
venv_tkinter\Scripts\activate   # For Windows
```

### 3. Run the Application

```bash
python gui_app.py
```

## 📌 Usage

* Add books by entering Title, Author, and ISBN.
* Select eBook for digital books and specify download size.
* Lend, Return, and Remove books using buttons.

## 📌 License

This project is for educational purposes only.
