# Program 10: Reverse a list without using the reverse() method

numbers = []
n = int(input("How many numbers? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Original list:", numbers)

reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)
