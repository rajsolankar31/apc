class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __sub__(self, o): return Vector(self.x - o.x, self.y - o.y)
    def __mul__(self, k): return Vector(self.x * k, self.y * k)
    def __eq__(self, o): return self.x == o.x and self.y == o.y
    def __str__(self): return f"({self.x}, {self.y})"

a, b = Vector(2, 3), Vector(4, 1)
print(a + b, a - b, a * 3, a == b)
