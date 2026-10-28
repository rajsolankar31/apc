stock = {1: 10, 2: 25}
def in_stock(pid): return stock.get(pid, 0) > 0
