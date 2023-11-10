import unittest

from ex6 import sum_seq

class TestSumSeq(unittest.TestCase):
  def test_sum_seq_basic(self):
    my_sequence = [1, 2, [3, 4, (5, 6)], 7, [8, 9]]
    result = sum_seq(my_sequence)
    self.assertEqual(result, 45)

  def test_sum_seq_empty(self):
    my_sequence = []
    result = sum_seq(my_sequence)
    self.assertEqual(result, 0)

  def test_sum_seq_nested_empty(self):
    my_sequence = [1, [2, [], [3, [4, []]]]]
    result = sum_seq(my_sequence)
    self.assertEqual(result, 10)

if __name__ == '__main__':
  unittest.main()
