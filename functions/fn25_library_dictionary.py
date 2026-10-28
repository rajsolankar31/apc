books = {}   # book_id -> {"title": ..., "available": True/False}
def add_book(bid, title): books[bid] = {"title": title, "available": True}
def issue_book(bid):
    if bid in books and books[bid]["available"]: books[bid]["available"] = False; print("Issued:", books[bid]["title"])
    else: print("Book not available")
def return_book(bid):
    if bid in books and not books[bid]["available"]: books[bid]["available"] = True; print("Returned:", books[bid]["title"])
    else: print("Invalid return")
def search_book(title):
    return [b for b, d in books.items() if title.lower() in d["title"].lower()]
def display_available():
    for b, d in books.items():
        if d["available"]: print(b, d["title"])
add_book(1, "Python Basics"); add_book(2, "Data Structures"); add_book(3, "Algorithms")
issue_book(2); issue_book(2); print("Search 'python':", search_book("python"))
print("Available:"); display_available()
return_book(2); print("After return:"); display_available()
