def simple_interest(p, rate, years): return p * rate * years / 100
def emi(p, annual_rate, months):
    r = annual_rate / 12 / 100
    return p / months if r == 0 else p * r * (1 + r) ** months / ((1 + r) ** months - 1)
