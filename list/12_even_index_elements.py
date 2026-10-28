# Program 12: Even Index Elements
# Display all elements present at even index positions

numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Original list:", numbers)
print("Elements at even index positions:")
for i in range(0, len(numbers), 2):
    print(f"Index {i}: {numbers[i]}")
