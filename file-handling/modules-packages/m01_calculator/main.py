import calculator
a = float(input("First number: ")); b = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")
ops = {"+": calculator.add, "-": calculator.subtract, "*": calculator.multiply, "/": calculator.divide}
print("Result:", ops[op](a, b) if op in ops else "Invalid operation")
