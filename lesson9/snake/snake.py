from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def move(self):
    for segment in range(len(self.segments) - 1, 0 , -1):
      new_position = self.segments[segment - 1].position()
      self.segments[segment].goto(new_position)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  def add_segment(self, position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

  def sub_segment(self):
    if len(self.segments) > 1:
      last_segment = self.segments[-1]
      last_segment.goto(1000, 1000)  # Przenosimy segment poza ekran
      self.segments.pop()  # Usuwamy ostatni segment z listy

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def reduce(self):
    self.sub_segment()

  def reset(self):
    for segment in self.segments:
      segment.goto(1000, 1000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]
