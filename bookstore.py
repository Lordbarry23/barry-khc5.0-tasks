import json
import os
import math

# File to save inventory
inventory_file = "books.json"

# Load books from file
def load_books():
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as f:
            return json.load(f)
    return []

# Save books to file
def save_books(books):
    with open(inventory_file, "w") as f:
        json.dump(books, f, indent=4)

# Add a new book
def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    price = float(input("Enter book price: "))
    stock = int(input("Enter number of copies in stock: "))

    book = {
        "title": title,
        "author": author,
        "price": round(price, 2),
        "stock": stock
    }

    books.append(book)
    save_books(books)
    print("Book added successfully!\n")

# View all books
def view_books(books):
    if not books:
        print("No books in inventory.\n")
        return

    for book in books:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Price: $", format(book["price"], ".2f"))
        print("Stock:", book["stock"])
        print("-" * 20)

# Main menu
books = load_books()

while True:
    print("=== Bookstore Inventory ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_book(books)
    elif choice == "2":
        view_books(books)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")