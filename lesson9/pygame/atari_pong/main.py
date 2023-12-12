import pygame
import random
from paddle import Paddle
from ball import Ball

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
INITIAL_BALL_SPEED = 3
BALL_SPEED_INCREASE = 0.2
WINNING_SCORE = 11

# Game variables
player1_score = 0
player2_score = 0
game_mode = None  # None: Menu, '1P': 1 Player, '2P': 2 Players

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Menu text
font = pygame.font.Font(None, 36)
menu_text1 = font.render("Press 1 for 1 Player", True, WHITE)
menu_text2 = font.render("Press 2 for 2 Players", True, WHITE)
menu_rect1 = menu_text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
menu_rect2 = menu_text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

# Create paddles and ball
player1_paddle = Paddle(20, HEIGHT // 2)
player2_paddle = Paddle(WIDTH - 20, HEIGHT // 2)
ball = Ball()

# Sprites group
all_sprites = pygame.sprite.Group()
all_sprites.add(player1_paddle, player2_paddle, ball)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        game_mode = '1P'
      elif event.key == pygame.K_2:
        game_mode = '2P'

  keys = pygame.key.get_pressed()

  # Game mode logic
  if game_mode == '1P':
    # Single player logic
    if keys[pygame.K_w]:
      player1_paddle.move("up")
    if keys[pygame.K_s]:
      player1_paddle.move("down")

    # Computer AI
    if ball.rect.centery < player2_paddle.rect.centery:
      player2_paddle.move("up")
    elif ball.rect.centery > player2_paddle.rect.centery:
      player2_paddle.move("down")
  elif game_mode == '2P':
    # Two players logic
    if keys[pygame.K_w]:
      player1_paddle.move("up")
    if keys[pygame.K_s]:
      player1_paddle.move("down")

    if keys[pygame.K_UP]:
      player2_paddle.move("up")
    if keys[pygame.K_DOWN]:
      player2_paddle.move("down")
  else:
    # Display menu
    screen.fill(BLACK)
    screen.blit(menu_text1, menu_rect1)
    screen.blit(menu_text2, menu_rect2)

    # Update display
    pygame.display.flip()
    continue  # Skip the rest of the loop when in menu mode

  # Move the ball
  ball.move()

  # Check collisions with paddles
  if pygame.sprite.collide_rect(ball, player1_paddle) or pygame.sprite.collide_rect(ball, player2_paddle):
    ball.dx *= -1
    ball.speed += BALL_SPEED_INCREASE

  # Check if the ball hits the walls
  if ball.rect.left <= 0:
    player2_score += 1
    ball.rect.center = (WIDTH // 2, HEIGHT // 2)
    ball.dx *= -1
    ball.speed = INITIAL_BALL_SPEED
  elif ball.rect.right >= WIDTH:
    player1_score += 1
    ball.rect.center = (WIDTH // 2, HEIGHT // 2)
    ball.dx *= -1
    ball.speed = INITIAL_BALL_SPEED

  # Draw everything
  screen.fill(BLACK)
  all_sprites.draw(screen)

  # Display scores
  font = pygame.font.Font(None, 36)
  score_text = font.render(f"{player1_score} - {player2_score}", True, WHITE)
  screen.blit(score_text, (WIDTH // 2 - 20, 10))

  if player1_score == WINNING_SCORE or player2_score == WINNING_SCORE:
    # Display winner text
    winner_text = font.render(f"Player {1 if player1_score == WINNING_SCORE else 2} wins!", True, (255, 255, 255))
    screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    pygame.display.flip()

    # Wait for a moment before quitting
    pygame.time.delay(2000)
    running = False

  # Update display
  pygame.display.flip()

  # Set the frame rate
  clock.tick(FPS)

# Quit Pygame
pygame.quit()
