import unittest

from ex7 import flatten

class TestFlatten(unittest.TestCase):
  def test_flatten_basic(self):
    seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    result = flatten(seq)
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.assertEqual(result, expected_result)

  def test_flatten_empty(self):
    seq = []
    result = flatten(seq)
    self.assertEqual(result, [])

  def test_flatten_nested_empty(self):
    seq = [1, (2, [], [3, [4, []]])]
    result = flatten(seq)
    expected_result = [1, 2, 3, 4]
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()
