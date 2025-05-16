# Library Management System (PyQt)

## 📌 Project Overview

This is a GUI-based Library Management System built using **PyQt5** in Python. It allows users to add, lend, return, and remove books from the library. It also supports eBooks with download sizes.

## 🚀 Features

* Add, Lend, Return, and Remove Books.
* Support for both physical and eBooks.
* Custom error handling for unavailable books.
* eBook field is disabled until the checkbox is checked.
* Clean, user-friendly interface.

## 📂 Project Structure

```
├── book_library.py  # Core logic of the library
├── gui_app.py       # GUI interface using PyQt5
└── README.md        # Project instructions
```

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/LibraryManagement_PyQt.git
cd LibraryManagement_PyQt
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv_pyqt
source venv_pyqt/bin/activate  # For Mac/Linux
venv_pyqt\Scripts\activate   # For Windows

pip install pyqt5
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
