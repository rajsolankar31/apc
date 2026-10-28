# Program 13: Sort in Ascending and Descending Order
# Accept 10 numbers and sort in ascending and descending order

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Original list:", numbers)
asc = sorted(numbers)
desc = sorted(numbers, reverse=True)
print("Ascending order:", asc)
print("Descending order:", desc)
