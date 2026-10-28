def electricity_bill(units):
    # 1-100: Rs5, 101-200: Rs7, above 200: Rs10 per unit
    if units <= 100: return units * 5
    if units <= 200: return 500 + (units - 100) * 7
    return 500 + 700 + (units - 200) * 10
print("Bill: Rs.", electricity_bill(int(input("Units consumed: "))))
