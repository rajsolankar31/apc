class Father:
    def skills(self): print("Father: gardening")
class Mother:
    def skills(self): print("Mother: painting")
class Child(Father, Mother):
    def skills(self):
        super().skills()        # follows MRO: Father first
        Mother.skills(self)
        print("Child: coding")

Child().skills()
print("MRO:", [c.__name__ for c in Child.__mro__])
