class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Constructor: {name} created")

    def __del__(self):
        print(f"Destructor: {self.name} destroyed")

d = Demo("Object1")
del d
d2 = Demo("Object2")
print("End of program")
