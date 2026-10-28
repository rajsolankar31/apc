class Calculator:
    # Python has no true overloading; default/variable arguments are used instead
    def add(self, a, b=0, c=0): return a + b + c
    def area(self, *dims):
        if len(dims) == 1: return 3.14159 * dims[0] ** 2   # circle
        if len(dims) == 2: return dims[0] * dims[1]         # rectangle
        return "Invalid arguments"

c = Calculator()
print(c.add(5), c.add(5, 10), c.add(5, 10, 15))
print(c.area(3), c.area(4, 5))
