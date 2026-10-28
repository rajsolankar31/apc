def gross_salary(basic, hra_pct=20, da_pct=10):
    return basic + basic * hra_pct / 100 + basic * da_pct / 100
def deductions(basic, pf_pct=12, tax_pct=10):
    return basic * pf_pct / 100 + basic * tax_pct / 100
def net_salary(basic):
    return gross_salary(basic) - deductions(basic)
