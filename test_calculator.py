import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(4,3),7)
        self.assertEqual(self.calc.add(9,3),12)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(9,5),4)
        self.assertEqual(self.calc.subtract(8,3),5)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,4),8)
        self.assertEqual(self.calc.multiply(3,5),15)
    def test_divided(self):
        self.assertEqual(self.calc.divide(2,2),1)
        self.assertEqual(self.calc.divide(12,2),6)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(2,2),0)
        self.assertEqual(self.calc.modulo(13,2),1)
   
    
        

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main(verbosity=2)