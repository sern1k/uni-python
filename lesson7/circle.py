from points import Point
import math

class Circle:
  """Klasa reprezentująca okręgi na płaszczyźnie."""

  def __init__(self, x, y, radius):
    if radius < 0:
      raise ValueError("Promień nie może być ujemny")
    self.pt = Point(x, y)
    self.radius = radius

  def __repr__(self):
    return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

  def __eq__(self, other):
    return self.pt == other.pt and self.radius == other.radius

  def __ne__(self, other):
    return not self == other

  def area(self):
    return math.pi * self.radius**2

  def move(self, x, y):
    self.pt.x += x
    self.pt.y += y

  def cover(self, other):
    distance = math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)
    new_radius = max(self.radius, other.radius, distance / 2)
    new_x = (self.pt.x + other.pt.x) / 2
    new_y = (self.pt.y + other.pt.y) / 2
    return Circle(new_x, new_y, new_radius)

c1 = Circle(1, 0, 45)
c2 = Circle(1, 3, 45)
print(c1 == c2)
print(c1.area())
print(c1.cover(c2))
print("\nC1 was moved - (0,3)\n")
c1.move(0,3)
print(c1 == c2)
print(c1.area())
print(c1.cover(c2))
