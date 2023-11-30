from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(5, 1)
    self.penup()
    self.goto(position)

  def go_up(self):
    new_y = self.ycor() + 20
    if new_y < 280:
      self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 20
    if new_y > -280:
      self.goto(self.xcor(), new_y)

  def track_ball(self, ball):
    # Sprawdź, czy piłka jest powyżej czy poniżej paletki
    if ball.ycor() > self.ycor():
      self.go_up()
    elif ball.ycor() < self.ycor():
      self.go_down()
