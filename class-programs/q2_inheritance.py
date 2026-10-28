class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}\nSalary: {self.salary}")
        self.display_person_info()

e = Employee("Amit", 28, "E101", 60000)
e.display_employee_info()
