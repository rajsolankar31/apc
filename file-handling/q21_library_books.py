import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
FIELDS = ["BookID", "Title", "Author", "Status"]
def load():
    with open("books.txt") as f: return list(csv.DictReader(f))
def save(b):
    with open("books.txt", "w", newline="") as f:
        w = csv.DictWriter(f, FIELDS); w.writeheader(); w.writerows(b)
def add_book(b):
    new_id = str(max([int(x["BookID"]) for x in b], default=0) + 1)
    b.append({"BookID": new_id, "Title": input("Title: "), "Author": input("Author: "), "Status": "Available"})
    save(b); print("Book added.")
def search(b):
    t = input("Search title/author: ").lower()
    for x in b:
        if t in x["Title"].lower() or t in x["Author"].lower(): print(x)
def change(b, status, need):
    i = input("Book ID: ")
    for x in b:
        if x["BookID"] == i:
            if x["Status"] == need: x["Status"] = status; save(b); print("Done.")
            else: print(f"Cannot: book is {x['Status']}.")
            return
    print("Book not found.")
def available(b):
    for x in b:
        if x["Status"] == "Available": print(x["BookID"], x["Title"], "-", x["Author"])
while True:
    books = load()
    c = input("\n1.Add 2.Search 3.Issue 4.Return 5.Available 6.Exit: ")
    if c == "1": add_book(books)
    elif c == "2": search(books)
    elif c == "3": change(books, "Issued", "Available")
    elif c == "4": change(books, "Available", "Issued")
    elif c == "5": available(books)
    elif c == "6": break
