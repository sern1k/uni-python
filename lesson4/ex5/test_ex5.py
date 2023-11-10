import unittest

from ex5_iteracyjnie import reverse_iter
from ex5_rekurencyjnie import reverse_rec

class TestReverse(unittest.TestCase):
  def test_reverse_positive_iter(self):
    L = [1, 2, 3, 4, 5]
    result = reverse_iter(L, 1, 3)
    expected_result = [1, 4, 3, 2, 5]
    self.assertEqual(result, expected_result)

  def test_reverse_negative_iter(self):
    L = [1, 2, 3, 4, 5]
    result = reverse_iter(L, -1, 3)
    self.assertEqual(result, L)
    result = reverse_iter(L, 0, 5)
    self.assertEqual(result, L)

  def test_reverse_positive_rec(self):
    L = [1, 2, 3, 4, 5]
    result = reverse_rec(L, 1, 3)
    expected_result = [1, 4, 3, 2, 5]
    self.assertEqual(result, expected_result)

  def test_reverse_negative_rec(self):
    L = [1, 2, 3, 4, 5]
    result = reverse_rec(L, -1, 3)
    self.assertEqual(result, L)
    result = reverse_rec(L, 0, 5)
    self.assertEqual(result, L)

if __name__ == '__main__':
  unittest.main()
