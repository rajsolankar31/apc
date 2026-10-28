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

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        print(f"Department: {self.department}\nTeam Size: {self.team_size}")
        self.display_employee_info()

m = Manager("Priya", 35, "M201", 120000, "IT", 12)
m.display_manager_info()
