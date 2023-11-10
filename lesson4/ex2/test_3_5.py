import unittest

from ex3_5 import make_ruler

class TestMakeRuler(unittest.TestCase):
  def test_make_ruler_positive(self):
    result = make_ruler(5)
    expected_result = "|....|....|....|....|....|\n0    1    2    3    4    5   "
    self.assertEqual(result, expected_result)

  def test_make_ruler_negative(self):
    result = make_ruler(0)
    self.assertIsNone(result)

if __name__ == '__main__':
  unittest.main()
