class Student:
    def __init__(self, name, roll, marks):
        self.name, self.roll, self.marks = name, roll, marks

    def total(self): return sum(self.marks)
    def percentage(self): return self.total() / len(self.marks)
    def grade(self):
        p = self.percentage()
        return "A" if p >= 80 else "B" if p >= 60 else "C" if p >= 40 else "F"
    def display(self):
        print(f"{self.name} (Roll {self.roll}) Total: {self.total()} Percentage: {self.percentage():.1f}% Grade: {self.grade()}")

Student("Amit", 101, [85, 90, 78]).display()
Student("Priya", 102, [55, 48, 62]).display()
