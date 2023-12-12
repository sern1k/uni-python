import pygame
from snake import Snake
from fruit import Fruit, PoisonFruit
import time

class Game:
  def __init__(self):
    self.width = 800
    self.height = 600
    self.dis = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption('Snake Game')
    self.clock = pygame.time.Clock()
    self.snake = Snake(self.width, self.height)
    self.fruit = Fruit(self.width, self.height)
    self.poison_fruit = PoisonFruit(self.width, self.height)
    self.score = 0
    self.load_highscore()
    self.last_fruit_change_time = time.time()

  def run(self):
    game_over = False
    direction = "RIGHT"
    while not game_over:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_over = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT and direction != "RIGHT":
            direction = "LEFT"
          elif event.key == pygame.K_RIGHT and direction != "LEFT":
            direction = "RIGHT"
          elif event.key == pygame.K_UP and direction != "DOWN":
            direction = "UP"
          elif event.key == pygame.K_DOWN and direction != "UP":
            direction = "DOWN"

      self.snake.move(direction)
      self.check_collision()

      # Draw the background
      self.dis.fill((0, 0, 0))

      # Draw the snake
      for segment in self.snake.snake_list:
        pygame.draw.rect(self.dis, (255, 255, 255), [segment[0], segment[1], self.snake.snake_block, self.snake.snake_block])

      # Draw fruits
      current_time = time.time()
      if current_time - self.last_fruit_change_time >= 15:
        self.fruit.generate_new_fruit()
        self.poison_fruit.generate_new_fruit()
        self.last_fruit_change_time = current_time

      pygame.draw.rect(self.dis, self.fruit.fruit_color, [self.fruit.fruit_pos[0], self.fruit.fruit_pos[1], self.fruit.fruit_size, self.fruit.fruit_size])
      if len(self.poison_fruit.fruit_pos) > 0:
        pygame.draw.rect(self.dis, self.poison_fruit.fruit_color, [self.poison_fruit.fruit_pos[0], self.poison_fruit.fruit_pos[1], self.poison_fruit.fruit_size, self.poison_fruit.fruit_size])

      # Update display
      self.show_score()
      pygame.display.update()

      # Control snake speed
      self.clock.tick(self.snake.snake_speed)

    pygame.quit()

  def check_collision(self):
    # Check for collisions with itself
    for segment in self.snake.snake_list[:-1]:
      if segment == self.snake.snake_head:
        self.update_highscore()
        pygame.quit()
        quit()

    # Check for boundary conditions
    if self.snake.snake_head[0] < 0 or self.snake.snake_head[0] >= self.width or \
      self.snake.snake_head[1] < 0 or self.snake.snake_head[1] >= self.height:
      self.update_highscore()
      pygame.quit()
      quit()

    # Check for collisions with fruit
    if self.snake.snake_head[0] == self.fruit.fruit_pos[0] and \
      self.snake.snake_head[1] == self.fruit.fruit_pos[1]:
      self.snake.snake_length += 1
      self.fruit.generate_new_fruit()
      self.poison_fruit.generate_new_fruit()
      self.score += 1

    # Check for collisions with poison fruit
    if len(self.poison_fruit.fruit_pos) > 0 and \
      self.snake.snake_head[0] == self.poison_fruit.fruit_pos[0] and \
      self.snake.snake_head[1] == self.poison_fruit.fruit_pos[1]:
      self.score -= 1
      self.poison_fruit.generate_new_fruit()
      if self.score < 0:
        pygame.quit()
        quit()

  def save_highscore(self):
    with open("highscore.txt", "w") as file:
      file.write(str(self.highscore))

  def load_highscore(self):
    try:
      with open("highscore.txt", "r") as file:
        self.highscore = int(file.read())
    except FileNotFoundError:
      # Plik nie istnieje, więc highscore będzie domyślnie ustawiony na 0
      self.highscore = 0

  def update_highscore(self):
    if self.score > self.highscore:
      self.highscore = self.score
      self.save_highscore()

  def show_score(self):
    font = pygame.font.SysFont(None, 30)
    score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
    self.dis.blit(score_text, [10, 10])
    highscore_text = font.render("Highscore: " + str(self.highscore), True, (255, 255, 255))
    self.dis.blit(highscore_text, [100, 10])
