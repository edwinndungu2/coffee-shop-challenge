import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        c = Coffee("Espresso")
        self.assertEqual(c.name, "Espresso")

    def test_name_too_short(self):
        with self.assertRaises(ValueError):
            Coffee("Es")

    def test_name_is_immutable(self):
        c = Coffee("Latte")
        with self.assertRaises(AttributeError):
            c.name = "Mocha"

if __name__ == "__main__":
    unittest.main()
