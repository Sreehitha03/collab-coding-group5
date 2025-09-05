import unittest
from functions.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(fibonacci(5), 5)   # sequence: 0,1,1,2,3,5

    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-3)

if __name__ == "__main__":
    unittest.main()
