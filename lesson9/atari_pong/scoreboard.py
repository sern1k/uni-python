from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 80, "normal")
SMALLER_FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-100, 200)
    self.write(self.l_score, align=ALIGNMENT, font=FONT)
    self.goto(100, 200)
    self.write(self.r_score, align=ALIGNMENT, font=FONT)

  def l_point(self):
    self.l_score += 1
    self.update_scoreboard()

  def r_point(self):
    self.r_score += 1
    self.update_scoreboard()

  def display_winner(self):
    self.goto(0, 0)
    winner = "Left Player Wins!" if self.l_score == 11 else "Right Player Wins!"
    self.write(winner, align=ALIGNMENT, font=SMALLER_FONT)
