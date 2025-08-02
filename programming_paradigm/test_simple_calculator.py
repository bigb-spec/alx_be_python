import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()
        
    def test_add(self):
        """Test the addition method."""
        #Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        #Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3),-5)
        #Test zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        #Test floating-point number
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        
    def test_subtract(self):
        """Test subrtaction method."""
        #Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        #Test negative numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        #Test zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        #Test floating-point number
        self.assertAlmostEqual(self.calc.subtract(5.5, 3.5), 2.0)
        
    def test_multiply(self):
        """Test multiplication method."""
        #Test positive numbers
        self.assertEqual(self.calc.multiply(5, 3), 15)
        #Test negative numbers
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        #Test zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        #Test floating-point number
        self.assertAlmostEqual(self.calc.multiply(5.5, 3.5), 19.25)
        
    def test_divide(self):
        """Test division method."""
        #Test positive numbers
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        #Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(-6, -3), 2.0)
        #Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        #Test zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        #Test floating-point number
        self.assertAlmostEqual(self.calc.divide(10.0, 5.0), 2.0)

if __name__ == "__main__":
    unittest.main()