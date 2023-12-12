import pygame

class Paddle(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((10, 60))
    self.image.fill((255, 255, 255))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.speed = 5

  def move(self, direction):
    if direction == "up" and self.rect.top > 0:
      self.rect.y -= self.speed
    elif direction == "down" and self.rect.bottom < 400:
      self.rect.y += self.speed
