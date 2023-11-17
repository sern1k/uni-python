import unittest

from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):
  def test_str_representation(self):
    rectangle = Rectangle(1, 2, 3, 4)
    self.assertEqual(str(rectangle), "[(1, 2), (3, 4)]")

  def test_repr_representation(self):
    rectangle = Rectangle(1, 2, 3, 4)
    self.assertEqual(repr(rectangle), "Rectangle(1, 2, 3, 4)")

  def test_equality(self):
    rectangle1 = Rectangle(1, 2, 3, 4)
    rectangle2 = Rectangle(1, 2, 3, 4)
    self.assertEqual(rectangle1, rectangle2)

  def test_inequality(self):
    rectangle1 = Rectangle(1, 2, 3, 4)
    rectangle2 = Rectangle(5, 6, 7, 8)
    self.assertNotEqual(rectangle1, rectangle2)

  def test_center(self):
    rectangle = Rectangle(1, 2, 5, 6)
    result = rectangle.center()
    self.assertEqual(result, Point(3.0, 4.0))

  def test_area(self):
    rectangle = Rectangle(1, 2, 5, 6)
    result = rectangle.area()
    self.assertEqual(result, 16)

  def test_move(self):
    rectangle = Rectangle(1, 2, 3, 4)
    rectangle.move(2, 3)
    self.assertEqual(rectangle, Rectangle(3, 5, 5, 7))

if __name__ == '__main__':
  unittest.main()
