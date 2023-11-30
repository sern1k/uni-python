from rectangles import Rectangle
from points import Point
import pytest

def test_from_points():
  point1 = Point(1, 2)
  point2 = Point(3, 4)
  rectangle = Rectangle.from_points((point1, point2))
  assert rectangle == Rectangle(1, 2, 3, 4)

def test_attributes():
  rectangle = Rectangle(1, 2, 4, 6)
  assert rectangle.top == 6
  assert rectangle.left == 1
  assert rectangle.bottom == 2
  assert rectangle.right == 4
  assert rectangle.width == 3
  assert rectangle.height == 4
  assert rectangle.topleft == Point(1, 6)
  assert rectangle.bottomleft == Point(1, 2)
  assert rectangle.topright == Point(4, 6)
  assert rectangle.bottomright == Point(4, 2)

if __name__ == "__main__":
  pytest.main()
