import re
e = input("Enter email: ")
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
print("Valid email" if re.match(pattern, e) else "Invalid email")
