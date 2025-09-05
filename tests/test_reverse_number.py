import unittest
from functions.reverse_number import reverse_number

class TestReverseNumber(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(reverse_number(1234), 4321)
        self.assertEqual(reverse_number(9070), 709)   # Leading zeros removed

    def test_negative(self):
        self.assertEqual(reverse_number(-567), -765)

    def test_single_digit(self):
        self.assertEqual(reverse_number(5), 5)
        self.assertEqual(reverse_number(-8), -8)

    def test_zero(self):
        self.assertEqual(reverse_number(0), 0)

if __name__ == "__main__":
    unittest.main()
