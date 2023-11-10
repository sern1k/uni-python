import unittest

from ex4 import fibonacci

class TestFibonacci(unittest.TestCase):
  def test_fibonacci_positive(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(3), 2)
    self.assertEqual(fibonacci(4), 3)
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(6), 8)
    self.assertEqual(fibonacci(7), 13)
    self.assertEqual(fibonacci(8), 21)

  def test_fibonacci_negative(self):
    self.assertIsNone(fibonacci(-1))
    self.assertIsNone(fibonacci(-5))

if __name__ == '__main__':
  unittest.main()
