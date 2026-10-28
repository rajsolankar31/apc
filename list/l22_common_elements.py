a = input("First list: ").split(); b = input("Second list: ").split()
print("Common elements:", [x for x in dict.fromkeys(a) if x in b])
