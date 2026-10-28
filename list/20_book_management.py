# Program 20: Book Management
# List of books: add, search, remove, display, count

books = ["Python Basics", "Data Structures", "Algorithms"]
while True:
    print("\n--- Book Management Menu ---")
    print("1. Add a new book")
    print("2. Search a book")
    print("3. Remove a book")
    print("4. Display all books")
    print("5. Count total books")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print(f"'{book}' added.")
    elif choice == 2:
        book = input("Enter book name to search: ")
        if book in books:
            print(f"'{book}' found at index {books.index(book)}.")
        else:
            print(f"'{book}' not found.")
    elif choice == 3:
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print(f"'{book}' removed.")
        else:
            print(f"'{book}' not found.")
    elif choice == 4:
        print("Books:", books)
    elif choice == 5:
        print(f"Total books: {len(books)}")
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
