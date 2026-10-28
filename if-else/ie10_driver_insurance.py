married = input("Is the driver married? (y/n): ").lower() == "y"
age = int(input("Age: "))
gender = input("Gender (m/f): ").lower()
if married: insured = True
elif gender == "m" and age > 30: insured = True
elif gender == "f" and age > 25: insured = True
else: insured = False
print("Driver is insured" if insured else "Driver is not insured")
