import unittest
import math

from circle import Circle

class TestCircle(unittest.TestCase):
  def test_valid_circle(self):
    circle = Circle(1, 2, 3)
    self.assertEqual(repr(circle), "Circle(1, 2, 3)")

  def test_invalid_radius(self):
    with self.assertRaises(ValueError):
      Circle(1, 2, -3)

  def test_equality(self):
    circle1 = Circle(1, 2, 3)
    circle2 = Circle(1, 2, 3)
    circle3 = Circle(0, 0, 5)

    self.assertEqual(circle1, circle2)
    self.assertNotEqual(circle1, circle3)

  def test_area(self):
    circle = Circle(0, 0, 5)
    self.assertAlmostEqual(circle.area(), 25 * math.pi, places=5)

  def test_move(self):
    circle = Circle(1, 1, 2)
    circle.move(2, 3)
    self.assertEqual(circle, Circle(3, 4, 2))

  def test_cover(self):
    circle1 = Circle(0, 0, 5)
    circle2 = Circle(4, 4, 2)
    covered_circle = circle1.cover(circle2)
    self.assertEqual(repr(covered_circle), "Circle(2.0, 2.0, 5)")

if __name__ == '__main__':
  unittest.main()
