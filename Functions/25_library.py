books = {}


def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}


def issue_book(book_id):
    if book_id not in books:
        return "Book not found"
    if not books[book_id]["available"]:
        return "Book is already issued"
    books[book_id]["available"] = False
    return "Book issued"


def return_book(book_id):
    if book_id not in books:
        return "Book not found"
    books[book_id]["available"] = True
    return "Book returned"


def search_books(keyword):
    return [book for book in books.values() if keyword.lower() in book["title"].lower()]


def available_books():
    return [book for book in books.values() if book["available"]]


add_book(1, "The Alchemist")
add_book(2, "The Hobbit")
issue_book(1)
print(search_books("the"))
print(available_books())
