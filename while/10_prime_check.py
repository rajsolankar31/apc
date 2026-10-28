# Program 10: Check if the entered number is prime or not using while loop

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is NOT a prime number.")
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f"{num} is a PRIME number.")
    else:
        print(f"{num} is NOT a prime number.")
