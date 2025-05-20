import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        customer = Customer("Chloe")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 5.5)

        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.5)

    def test_invalid_price(self):
        customer = Customer("Max")
        coffee = Coffee("Latte")

        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(customer, coffee, 15.0)

    def test_invalid_types(self):
        coffee = Coffee("Mocha")
        customer = Customer("Zara")

        with self.assertRaises(TypeError):
            Order("NotCustomer", coffee, 5.0)

        with self.assertRaises(TypeError):
            Order(customer, "NotCoffee", 5.0)

if __name__ == "__main__":
    unittest.main()
