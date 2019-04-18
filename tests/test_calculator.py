import unittest
import os
import sys
sys.path.append(os.path.abspath("."))


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator_depreciated.add(10, 5), 15)
        self.assertEqual(calculator_depreciated.add(-1, 1), 0)
        self.assertEqual(calculator_depreciated.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator_depreciated.subtract(10, 5), 5)
        self.assertEqual(calculator_depreciated.subtract(-1, 1), -2)
        self.assertEqual(calculator_depreciated.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator_depreciated.multiply(10, 5), 50)
        self.assertEqual(calculator_depreciated.multiply(-1, 1), -1)
        self.assertEqual(calculator_depreciated.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calculator_depreciated.divide(10, 5), 2)
        self.assertEqual(calculator_depreciated.divide(-1, 1), -1)
        self.assertEqual(calculator_depreciated.divide(-1, -1), 1)
        self.assertEqual(calculator_depreciated.divide(5, 2), 2.5)

if __name__ == '__main__':
    unittest.main()


