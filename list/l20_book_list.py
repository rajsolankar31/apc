books = ["Python Basics", "Data Structures"]
while True:
    print("\n1.Add 2.Search 3.Remove 4.Display 5.Count 6.Exit")
    c = input("Choice: ")
    if c == "1": books.append(input("Book name: "))
    elif c == "2": print("Found" if input("Search book: ") in books else "Not found")
    elif c == "3":
        b = input("Book to remove: ")
        if b in books: books.remove(b)
        else: print("Book not found")
    elif c == "4": print(books)
    elif c == "5": print("Total books:", len(books))
    elif c == "6": break
