import unittest

from points import Point

class TestPoint(unittest.TestCase):
  def setUp(self):
    self.point_a = Point(1, 0)
    self.point_b = Point(2, 3)
    self.point_c = Point(2, 1)
    self.point_d = Point(1, 0)

  def test_str_representation(self):
    self.assertEqual(str(self.point_a), "(1, 0)")

  def test_repr_representation(self):
    self.assertEqual(repr(self.point_a), "Point(1, 0)")

  def test_equality(self):
    self.assertEqual(self.point_a, self.point_d)
    self.assertNotEqual(self.point_a, self.point_b)

  def test_inequality(self):
    self.assertNotEqual(self.point_a, self.point_b)

  def test_vector_addition(self):
    self.assertEqual(self.point_a + self.point_b, Point(3, 3))

  def test_vector_subtraction(self):
    self.assertEqual(self.point_a - self.point_b, Point(-1, -3))

  def test_scalar_multiplication(self):
    self.assertEquals((self.point_a * self.point_b), 2)
    self.assertEquals((self.point_a * self.point_d), 1)

  def test_cross_product(self):
    self.assertEqual(self.point_a.cross(self.point_d), 0)
    self.assertEqual(self.point_a.cross(self.point_c), 1)

  def test_vector_length(self):
    self.assertEqual(self.point_a.length(), 1.0)
    self.assertEqual(self.point_c.length(), 2.23606797749979)

  def test_hash(self):
    self.assertEqual(hash(self.point_a), -5164621852614943976)

if __name__ == '__main__':
  unittest.main()
