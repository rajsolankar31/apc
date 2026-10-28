def gross_salary(basic, hra_pct=20, da_pct=10):
    return basic + basic * hra_pct / 100 + basic * da_pct / 100
print("Gross salary:", gross_salary(float(input("Basic salary: "))))
