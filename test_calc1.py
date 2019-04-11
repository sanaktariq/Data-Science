import unittest
import calc1

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc1.add(10, 5), 15)
        self.assertEqual(calc1.add(-1, 1), 0)
        self.assertEqual(calc1.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc1.subtract(10, 5), 5)
        self.assertEqual(calc1.subtract(-1, 1), -2)
        self.assertEqual(calc1.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc1.multiply(10, 5), 50)
        self.assertEqual(calc1.multiply(-1, 1), -1)
        self.assertEqual(calc1.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc1.divide(10, 5), 2)
        self.assertEqual(calc1.divide(-1, 1), -1)
        self.assertEqual(calc1.divide(-1, -1), 1)
        self.assertEqual(calc1.divide(5.0, 2.0), 2.5)

if __name__ == '__main__':
    unittest.main()


