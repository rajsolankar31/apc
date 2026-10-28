class Student:
    count = 0          # class variable, shared
    college = "ABC College"

    def __init__(self, name):
        self.name = name   # instance variable, per object
        Student.count += 1

s1, s2, s3 = Student("Amit"), Student("Priya"), Student("Rahul")
print("Total students:", Student.count)
print(s1.name, s2.name, s3.name, "-", Student.college)
s1.college = "XYZ College"   # creates an instance variable only for s1
print(s1.college, "|", s2.college)
