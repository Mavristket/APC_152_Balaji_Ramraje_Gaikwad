import csv
import os

file_name = "books.csv"

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["BookID", "Title", "Author", "Available"])


def read_books():
    with open(file_name, "r", newline="") as file:
        return list(csv.DictReader(file))


def save_books(books):
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["BookID", "Title", "Author", "Available"])
        writer.writeheader()
        writer.writerows(books)


def find_book(books, book_id):
    return next((book for book in books if book["BookID"] == book_id), None)


books = read_books()
while True:
    print("\n1. Add  2. Search  3. Issue  4. Return  5. Available  6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        book = {
            "BookID": input("Book ID: "),
            "Title": input("Title: "),
            "Author": input("Author: "),
            "Available": "Yes",
        }
        books.append(book)
        save_books(books)
    elif choice == "2":
        book = find_book(books, input("Book ID: "))
        print(book if book else "Book not found.")
    elif choice in ("3", "4"):
        book = find_book(books, input("Book ID: "))
        if book:
            book["Available"] = "No" if choice == "3" else "Yes"
            save_books(books)
            print("Book updated.")
        else:
            print("Book not found.")
    elif choice == "5":
        for book in books:
            if book["Available"] == "Yes":
                print(book)
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
