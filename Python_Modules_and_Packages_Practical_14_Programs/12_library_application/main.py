from library.Books.books import *
from library.Members.members import *
from library.Transactions.transactions import *
add_book(101,"Python"); add_book(102,"Java"); add_member(1,"Amit")
print("Books:"); display_books(); print("Members:"); display_members()
issue_book("Python","Amit"); return_book("Python")
