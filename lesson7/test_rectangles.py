import unittest

from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):

  def test_valid_rectangle(self):
    rect = Rectangle(1, 2, 3, 4)
    self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

  def test_invalid_rectangle(self):
    with self.assertRaises(ValueError):
      Rectangle(3, 4, 1, 2)

  def test_center(self):
    rect = Rectangle(0, 0, 4, 4)
    self.assertEqual(rect.center(), Point(2, 2))

  def test_area(self):
    rect = Rectangle(0, 0, 3, 5)
    self.assertEqual(rect.area(), 15)

  def test_move(self):
    rect = Rectangle(1, 1, 3, 3)
    rect.move(2, 3)
    self.assertEqual(rect, Rectangle(3, 4, 5, 6))

  def test_intersection(self):
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(3, 2, 6, 5)
    intersection_rect = rect1.intersection(rect2)
    self.assertEqual(str(intersection_rect), "[(3, 2), (4, 4)]")

  def test_cover(self):
    rect1 = Rectangle(1, 1, 3, 3)
    rect2 = Rectangle(2, 2, 4, 4)
    cover_rect = rect1.cover(rect2)
    self.assertEqual(str(cover_rect), "[(1, 1), (4, 4)]")

  def test_make4(self):
    rect = Rectangle(1, 1, 4, 4)
    smaller_rectangles = rect.make4()
    self.assertEqual(len(smaller_rectangles), 4)

if __name__ == '__main__':
  unittest.main()
