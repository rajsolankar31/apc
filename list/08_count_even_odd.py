# Program 8: Store 15 integers in a list and count how many are even and how many are odd

numbers = []

for i in range(15):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", numbers)
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
