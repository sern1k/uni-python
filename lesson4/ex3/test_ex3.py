import unittest

from ex3 import factorial

class TestFactorial(unittest.TestCase):
  def test_factorial_positive(self):
    self.assertEqual(factorial(0), 1)
    self.assertEqual(factorial(1), 1)
    self.assertEqual(factorial(2), 2)
    self.assertEqual(factorial(3), 6)
    self.assertEqual(factorial(4), 24)
    self.assertEqual(factorial(5), 120)
    self.assertEqual(factorial(6), 720)

  def test_factorial_negative(self):
    self.assertIsNone(factorial(-1))
    self.assertIsNone(factorial(-5))

if __name__ == '__main__':
  unittest.main()
