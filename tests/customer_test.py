import unittest
from customer import Customer
from coffee import Coffee

class DummyOrder:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

class TestCustomer(unittest.TestCase):
    def test_valid_name(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")

    def test_name_setter(self):
        c = Customer("Bob")
        c.name = "Charlie"
        self.assertEqual(c.name, "Charlie")

    def test_name_setter_invalid(self):
        c = Customer("Bob")
        with self.assertRaises(ValueError):
            c.name = ""
        with self.assertRaises(TypeError):
            c.name = 123

    def test_orders_initially_empty(self):
        c = Customer("Dana")
        self.assertEqual(c.orders(), [])

    def test_create_order(self):
        c = Customer("Eve")
        coffee = Coffee("Mocha")
        order = c.create_order(coffee, 4.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertEqual(c.orders()[0], order)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.5)
        self.assertIn(order, coffee.orders())

    def test_coffees(self):
        c = Customer("Frank")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        c.create_order(coffee1, 3.0)
        c.create_order(coffee2, 2.5)
        c.create_order(coffee1, 3.5)
        self.assertCountEqual(c.coffees(), [coffee1, coffee2])

if __name__ == "__main__":
    unittest.main()
