def consultation(days): return 500 * days
def laboratory(tests): return 800 * tests
def medicine(amount): return amount
def room(days, kind): return days * {"general": 1500, "private": 4000}.get(kind, 1500)
def discount_pct(category): return {"general": 0, "senior": 10, "staff": 20}.get(category, 0)
def final_bill(c, l, m, r, cat):
    total = c + l + m + r
    return total - total * discount_pct(cat) / 100
days = int(input("Days admitted: ")); tests = int(input("Lab tests: ")); med = float(input("Medicine charges: "))
kind = input("Room (general/private): ").lower(); cat = input("Category (general/senior/staff): ").lower()
print("Final bill: Rs.", final_bill(consultation(days), laboratory(tests), medicine(med), room(days, kind), cat))
