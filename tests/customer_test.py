import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_valid_customer_name(self):
        cust = Customer("Alice")
        self.assertEqual(cust.name, "Alice")

    def test_invalid_customer_name_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_invalid_customer_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("A" * 20)

    def test_create_order_and_coffees(self):
        cust = Customer("Bob")
        coffee = Coffee("Americano")
        cust.create_order(coffee, 4.5)

        self.assertEqual(len(cust.orders()), 1)
        self.assertIn(coffee, cust.coffees())

if __name__ == "__main__":
    unittest.main()

