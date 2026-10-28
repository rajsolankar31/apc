def total_bill(prices, quantities, discount_pct):
    subtotal = sum(p * q for p, q in zip(prices, quantities))
    return subtotal - subtotal * discount_pct / 100
prices = [float(x) for x in input("Item prices: ").split()]
qty = [int(x) for x in input("Quantities: ").split()]
d = float(input("Discount %: ")); print("Total bill:", total_bill(prices, qty, d))
