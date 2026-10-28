# Program 14: Print multiplication table using while loop

num = int(input("Enter a number: "))

i = 1
print(f"Multiplication table of {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
