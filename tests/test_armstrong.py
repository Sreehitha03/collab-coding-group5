import unittest
from functions.armstrong import is_armstrong

class TestIsArmstrong(unittest.TestCase):
    def test_armstrong_numbers(self):
        self.assertTrue(is_armstrong(153))
        self.assertTrue(is_armstrong(370))
        self.assertTrue(is_armstrong(9474))

    def test_non_armstrong_numbers(self):
        self.assertFalse(is_armstrong(10))
        self.assertFalse(is_armstrong(123))
        self.assertFalse(is_armstrong(9475))

if __name__ == "__main__":
    unittest.main()
