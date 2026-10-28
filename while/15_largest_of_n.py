# Program 15: Print the largest of n numbers using while loop

n = int(input("How many numbers do you want to enter? "))

i = 1
largest = None
while i <= n:
    num = int(input(f"Enter number {i}: "))
    if largest is None or num > largest:
        largest = num
    i += 1

print(f"The largest number is: {largest}")
