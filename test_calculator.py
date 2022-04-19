from calculator import calculator
import unittest

class calculatorTests(unittest.TestCase):
  def test_add(self):
    calc = calculator()
    self.assertEqual(10, calc.add(7, 3))
    
if __name__ == '__main__':
    unittest.main()