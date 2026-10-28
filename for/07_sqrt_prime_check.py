# Program 7: Check whether the square root of a number is prime or not

import math

num = int(input("Enter a number: "))

sqrt_val = math.isqrt(num)

# Check if num is a perfect square
if sqrt_val * sqrt_val != num:
    print(f"{num} is not a perfect square.")
else:
    # Check if sqrt_val is prime
    if sqrt_val < 2:
        print(f"Square root of {num} is {sqrt_val}, which is NOT prime.")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(sqrt_val)) + 1):
            if sqrt_val % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"Square root of {num} is {sqrt_val}, which is PRIME.")
        else:
            print(f"Square root of {num} is {sqrt_val}, which is NOT prime.")
