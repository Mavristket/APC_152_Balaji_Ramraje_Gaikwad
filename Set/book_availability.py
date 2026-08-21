
available_books = {"Hamlet", "Macbeth", "Odyssey", "Frankenstein", "1984"}
requested_books = {"Macbeth", "Frankenstein", "Dracula", "1984", "The Hobbit"}

available_requests = requested_books.intersection(available_books)

print("Available books:", available_books)
print("Requested books:", requested_books)
print("Requested books that are available:", available_requests)
