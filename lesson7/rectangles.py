from points import Point

class Rectangle:
  """Klasa reprezentująca prostokąt na płaszczyźnie."""

  def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
    if x1 >= x2 or y1 >= y2:
      raise ValueError("Invalid rectangle coordinates")
    self.pt1 = Point(x1, y1)
    self.pt2 = Point(x2, y2)

  def __str__(self):         # "[(x1, y1), (x2, y2)]"
    return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

  def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
    return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

  def __eq__(self, other):   # obsługa rect1 == rect2
    return self.pt1 == other.pt1 and self.pt2 == other.pt2

  def __ne__(self, other):        # obsługa rect1 != rect2
    return not self == other

  def center(self):          # zwraca środek prostokąta
    return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

  def area(self):            # pole powierzchni
    return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

  def move(self, x, y):      # przesunięcie o (x, y)
    self.pt1.x += x
    self.pt1.y += y
    self.pt2.x += x
    self.pt2.y += y

  def intersection(self, other): # część wspólna prostokątów
    x_min = max(self.pt1.x, other.pt1.x)
    y_min = max(self.pt1.y, other.pt1.y)
    x_max = min(self.pt2.x, other.pt2.x)
    y_max = min(self.pt2.y, other.pt2.y)

    if x_min >= x_max or y_min >= y_max:
      raise ValueError("Rectangles do not intersect")

    return Rectangle(x_min, y_min, x_max, y_max)

  def cover(self, other):    # prostąkąt nakrywający oba
    x_min = min(self.pt1.x, other.pt1.x)
    y_min = min(self.pt1.y, other.pt1.y)
    x_max = max(self.pt2.x, other.pt2.x)
    y_max = max(self.pt2.y, other.pt2.y)

    return Rectangle(x_min, y_min, x_max, y_max)

  def make4(self):           # zwraca krotkę czterech mniejszych
    center = self.center()

    rect_A = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
    rect_B = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
    rect_C = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
    rect_D = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)

    return rect_A, rect_B, rect_C, rect_D

rec1 = Rectangle(1, 0, 3, 3)
rec2 = Rectangle(1, 3, 2, 4)
print(rec1 == rec2)
print(rec1.center())
print(rec1.area())
print(rec1.make4())
