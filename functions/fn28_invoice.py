products = {}   # name -> (price, qty)
def add_product(name, price, qty): products[name] = (price, qty)
def remove_product(name): products.pop(name, None)
def subtotal(): return sum(p * q for p, q in products.values())
def apply_coupon(amount, code): return amount * 0.9 if code == "SAVE10" else amount
def gst(amount, rate=18): return amount * rate / 100
def invoice(code):
    sub = subtotal(); after = apply_coupon(sub, code); g = gst(after)
    print("----- INVOICE -----")
    for n, (p, q) in products.items(): print(f"{n:10} {p:8} x {q} = {p * q}")
    print(f"Subtotal: {sub}\nAfter coupon: {after}\nGST (18%): {g:.2f}\nFinal: {after + g:.2f}")
add_product("Pen", 10, 5); add_product("Notebook", 50, 3); add_product("Bag", 800, 1); remove_product("Pen")
invoice("SAVE10")
