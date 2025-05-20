from .customer import Customer
from .coffee import Coffee
from .order import Order

# Test initialization
customer1 = Customer("Alice")
customer2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Cappuccino")

# Test creating orders
order1 = Order(customer1, coffee1, 5.0)
order2 = Order(customer1, coffee2, 4.5)
order3 = Order(customer2, coffee1, 6.0)

# Test relationships
print(f"{customer1.name}'s orders: {[o.coffee.name for o in customer1.orders()]}")
print(f"{customer1.name}'s coffees: {[c.name for c in customer1.coffees()]}")
print(f"{coffee1.name}'s orders count: {coffee1.num_orders()}")
print(f"{coffee1.name}'s average price: {coffee1.average_price()}")