import unittest
from Calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(5,8), 13)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3,6), 17)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(25,5), 5)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(4,4), 0)
if __name__ == "__main__":
    unittest.main()
