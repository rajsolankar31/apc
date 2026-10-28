# Program 6: Find the largest and smallest number in a list without using max() or min()

numbers = []
n = int(input("How many numbers? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("List:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
