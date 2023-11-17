import unittest

from fracs import add_frac, sub_frac, mul_frac, div_frac, is_positive, is_zero, cmp_frac, frac2float

class TestFractions(unittest.TestCase):

  def setUp(self):
    self.zero = [0, 1]

  def test_add_frac(self):
    self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
    self.assertEqual(add_frac([1, 2], [1, -3]), [1, 6])
    self.assertEqual(add_frac([0, 2], [1, -3]), [1, -3])

  def test_sub_frac(self):
    self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
    self.assertEqual(sub_frac([1, 2], [1, -3]), [5, 6])
    self.assertEqual(sub_frac([0, 2], [1, -3]), [1, 3])

  def test_mul_frac(self):
    self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
    self.assertEqual(mul_frac([1, 2], [1, -3]), [-1, 6])
    self.assertEqual(mul_frac([0, 2], [1, -3]), [0, 1])

  def test_div_frac(self):
    self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
    self.assertEqual(div_frac([1, 2], [1, -3]), [-3, 2])
    self.assertEqual(div_frac([0, 2], [1, -3]), [0, 1])
    self.assertEqual(div_frac([1, -3], [0, 2]), "0 w mianowniku")

  def test_is_positive(self):
    self.assertEqual(is_positive([1, 2]), True)
    self.assertEqual(is_positive([1, -3]), False)
    self.assertEqual(is_positive([0, 2]), False)

  def test_is_zero(self):
    self.assertEqual(is_zero([1, 2]), False)
    self.assertEqual(is_zero([1, -3]), False)
    self.assertEqual(is_zero([0, 2]), True)

  def test_cmp_frac(self):
    self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
    self.assertEqual(cmp_frac([1, -2], [1, 3]), -1)
    self.assertEqual(cmp_frac([0, 2], [0, -3]), 0)

  def test_frac2float(self):
    self.assertEqual(frac2float([6, 2]), 3.0)
    self.assertEqual(frac2float([1, -2]), -0.5)
    self.assertEqual(frac2float([0, 2]), 0.0)

if __name__ == '__main__':
  unittest.main()     # uruchamia wszystkie testy
