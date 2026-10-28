def energy_charge(units):
    if units <= 100: return units * 5
    if units <= 200: return 500 + (units - 100) * 7
    return 500 + 700 + (units - 200) * 10
def fixed_charge(units): return 50 if units <= 100 else 100
def tax(amount, rate=5): return amount * rate / 100
def discount(amount, online): return amount * 0.02 if online else 0
units = int(input("Units consumed: ")); online = input("Paying online? (y/n): ").lower() == "y"
e = energy_charge(units); f = fixed_charge(units); t = tax(e + f); d = discount(e + f + t, online)
print(f"Energy: {e}\nFixed: {f}\nTax (5%): {t:.2f}\nDiscount: {d:.2f}\nTotal: {e + f + t - d:.2f}")
