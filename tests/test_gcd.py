import unittest
from functions.gcd import gcd

class TestGCD(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 25), 25)

    def test_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(7, 0), 7)

    def test_both_zero(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            gcd(-8, 12)
        with self.assertRaises(ValueError):
            gcd(15, -3)

if __name__ == "__main__":
    unittest.main()
