names, ages = [], []
while True:
    print("\n1.Add 2.Delete 3.Search 4.Display 5.Count 6.Exit")
    c = input("Choice: ")
    if c == "1": names.append(input("Name: ")); ages.append(int(input("Age: ")))
    elif c == "2":
        n = input("Patient to delete: ")
        if n in names: i = names.index(n); names.pop(i); ages.pop(i)
        else: print("Patient not found")
    elif c == "3":
        n = input("Search name: ")
        print(f"{n}, age {ages[names.index(n)]}" if n in names else "Not found")
    elif c == "4":
        for n, a in zip(names, ages): print(n, "-", a)
    elif c == "5": print("Total patients:", len(names))
    elif c == "6": break
