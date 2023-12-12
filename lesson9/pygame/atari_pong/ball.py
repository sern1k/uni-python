import pygame
import random

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((10, 10))
    self.image.fill((255, 255, 255))
    self.rect = self.image.get_rect()
    self.rect.center = (300, 200)
    self.speed = 3
    self.dx = random.choice([1, -1])
    self.dy = random.choice([1, -1])

  def move(self):
    self.rect.x += self.speed * self.dx
    self.rect.y += self.speed * self.dy

    # Bounce off walls
    if self.rect.top <= 0 or self.rect.bottom >= 400:
      self.dy *= -1
