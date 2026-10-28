def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b else "Cannot divide by zero"
def calculate(func, a, b): return func(a, b)
a = float(input("First: ")); b = float(input("Second: "))
for f in (add, subtract, multiply, divide): print(f.__name__, "->", calculate(f, a, b))
