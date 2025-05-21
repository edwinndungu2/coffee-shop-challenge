import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        cust = Customer("Clara")
        coffee = Coffee("Cappuccino")
        order = Order(cust, coffee, 5.0)

        self.assertEqual(order.customer, cust)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_price_type(self):
        with self.assertRaises(ValueError):
            Order(Customer("John"), Coffee("Latte"), "ten")

    def test_price_out_of_range(self):
        with self.assertRaises(ValueError):
            Order(Customer("John"), Coffee("Latte"), 0.5)

        with self.assertRaises(ValueError):
            Order(Customer("John"), Coffee("Latte"), 20.0)

if __name__ == "__main__":
    unittest.main()

