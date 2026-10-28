import math
class Shape:
    def area(self): return 0
    def describe(self): print(f"{self.__class__.__name__} area: {self.area():.2f}")

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2

class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w

for s in (Circle(5), Rectangle(4, 6), Shape()): s.describe()
