def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)): result *= base
    return result if exponent >= 0 else 1 / result
b = float(input("Base: ")); e = int(input("Exponent: ")); print(f"{b}^{e} =", power(b, e))
