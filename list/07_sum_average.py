# Program 7: Accept 10 numbers from the user, store in a list, calculate sum and average

numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("List:", numbers)
print(f"Sum = {total}")
print(f"Average = {average}")
