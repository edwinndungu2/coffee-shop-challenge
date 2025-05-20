import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_property(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")
        c.name = "Bob"
        self.assertEqual(c.name, "Bob")
        with self.assertRaises(ValueError):
            c.name = ""
        with self.assertRaises(TypeError):
            c.name = 123

    def test_create_order_and_lists(self):
        customer = Customer("Liam")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Mocha")

        customer.create_order(coffee1, 4.5)
        customer.create_order(coffee2, 5.0)
        customer.create_order(coffee1, 6.0)

        self.assertEqual(len(customer.orders()), 3)
        self.assertEqual(set(customer.coffees()), {coffee1, coffee2})

if __name__ == "__main__":
    unittest.main()
