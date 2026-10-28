from books.catalog import list_books
from members.registry import list_members
from transactions.issue import issue_book
from transactions.returns import return_book
print("Books:", list_books()); print("Members:", list_members())
print(issue_book(1, 2)); print(issue_book(1, 1)); print(return_book(1))
