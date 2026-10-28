# Program 18: Shopping Cart
# Shopping cart using a list: add, remove, search, display, count

cart = []
while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display cart")
    print("5. Count total items")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"{item} added to cart.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")
    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print(f"{item} is in the cart.")
        else:
            print(f"{item} is NOT in the cart.")
    elif choice == 4:
        print("Cart items:", cart)
    elif choice == 5:
        print(f"Total items in cart: {len(cart)}")
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
