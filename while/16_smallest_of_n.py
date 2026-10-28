# Program 16: Print the smallest of n numbers using while loop

n = int(input("How many numbers do you want to enter? "))

i = 1
smallest = None
while i <= n:
    num = int(input(f"Enter number {i}: "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1

print(f"The smallest number is: {smallest}")
