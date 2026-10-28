def factorial(n): return 1 if n <= 1 else n * factorial(n - 1)
def fibonacci(n): return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci_series(n): return [fibonacci(i) for i in range(n)]
def sum_of_digits(n): return n if n < 10 else n % 10 + sum_of_digits(n // 10)
def to_binary(n): return str(n) if n < 2 else to_binary(n // 2) + str(n % 2)
