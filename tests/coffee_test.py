import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("AB")

        c = Coffee("Cappuccino")
        self.assertEqual(c.name, "Cappuccino")

    def test_num_orders_and_avg_price(self):
        coffee = Coffee("Espresso")
        customer = Customer("Bob")

        customer.create_order(coffee, 5.0)
        customer.create_order(coffee, 7.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 6.0)

if __name__ == "__main__":
    unittest.main()
