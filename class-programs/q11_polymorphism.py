class Animal:
    def sound(self): return "Some sound"
class Dog(Animal):
    def sound(self): return "Woof"
class Cat(Animal):
    def sound(self): return "Meow"
class Cow(Animal):
    def sound(self): return "Moo"

for a in (Dog(), Cat(), Cow(), Animal()):
    print(f"{a.__class__.__name__}: {a.sound()}")
