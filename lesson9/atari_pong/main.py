from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Atari Pong")
screen.tracer(0)

game_mode = input("Wybierz tryb gry (1 - Komputer, 2 - 2 Graczy): ")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# 2 players
if game_mode == "2":
  screen.onkey(l_paddle.go_up, "w")
  screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  # Against computer
  if game_mode == "1":
    l_paddle.track_ball(ball)

  # Detect collisions with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # Detect collisions with r_paddle
  if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    ball.bounce_x()

  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()

  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

  if scoreboard.l_score == 11 or scoreboard.r_score == 11:
    game_is_on = False

scoreboard.display_winner()

screen.exitonclick()
