cart = []
while True:
    print("\n1.Add 2.Remove 3.Search 4.Display 5.Count 6.Exit")
    c = input("Choice: ")
    if c == "1": cart.append(input("Item: "))
    elif c == "2":
        i = input("Item to remove: ")
        if i in cart: cart.remove(i)
        else: print("Item not in cart")
    elif c == "3": print("Found" if input("Search item: ") in cart else "Not found")
    elif c == "4": print("Cart:", cart)
    elif c == "5": print("Total items:", len(cart))
    elif c == "6": break
