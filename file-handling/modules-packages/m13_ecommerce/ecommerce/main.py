from products.catalog import get_product, products
from products.inventory import in_stock
from customers.profile import get_customer
from customers.address import get_address
from orders.cart import cart_total
from orders.order import create_order
from payments.methods import METHODS
from payments.invoice import generate_invoice
print(get_customer(1), get_address(1))
items = [1, 2]
print("In stock:", [in_stock(i) for i in items])
total = cart_total(items, {k: v[1] for k, v in products.items()})
print(generate_invoice(create_order(1, items), total, METHODS[0]))
