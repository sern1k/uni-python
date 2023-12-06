from turtle import Turtle
import time

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(5, 1)
    self.penup()
    self.goto(position)
    self.last_move_time = time.time()
    self.move_delay = 0.07  # Ustawienie opóźnienia na 0.1 sekundy

  def go_up(self):
    current_time = time.time()
    if current_time - self.last_move_time > self.move_delay:
      new_y = self.ycor() + 20
      if new_y < 280:
        self.goto(self.xcor(), new_y)
        self.last_move_time = current_time

  def go_down(self):
    current_time = time.time()
    if current_time - self.last_move_time > self.move_delay:
      new_y = self.ycor() - 20
      if new_y > -280:
        self.goto(self.xcor(), new_y)
        self.last_move_time = current_time

  def track_ball(self, ball):
    # Sprawdź, czy piłka jest powyżej czy poniżej paletki
    if ball.ycor() > self.ycor():
      self.go_up()
    elif ball.ycor() < self.ycor():
      self.go_down()
