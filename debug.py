from customer import Customer
from coffee import Coffee

if __name__ == "__main__":
    c = Customer("Ed")
    coffee = Coffee("Espresso")
    order = c.create_order(coffee, 3.5)
    print(f"{c.name} ordered {coffee.name} for ${order.price}")
