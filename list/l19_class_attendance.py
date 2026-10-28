present = ["Amit", "Priya", "Rahul"]
while True:
    print("\n1.Total 2.Search 3.Add 4.Remove absent 5.Exit")
    c = input("Choice: ")
    if c == "1": print("Total students:", len(present))
    elif c == "2": n = input("Name: "); print(n, "is present" if n in present else "is not present")
    elif c == "3": present.append(input("New student: "))
    elif c == "4":
        n = input("Absent student to remove: ")
        if n in present: present.remove(n)
        else: print("Not in list")
    elif c == "5": break
