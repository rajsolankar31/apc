p = input("Enter password: "); errors = []
if len(p) < 8: errors.append("at least 8 characters")
if not any(c.isupper() for c in p): errors.append("an uppercase letter")
if not any(c.islower() for c in p): errors.append("a lowercase letter")
if not any(c.isdigit() for c in p): errors.append("a digit")
if not any(not c.isalnum() for c in p): errors.append("a special character")
print("Valid password" if not errors else "Invalid. Missing: " + ", ".join(errors))
