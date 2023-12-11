import random

class Fruit:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.fruit_size = 10
    self.fruit_color = (0, 255, 0)
    self.fruit_pos = [random.randrange(1, (width // self.fruit_size)) * self.fruit_size,
                      random.randrange(1, (height // self.fruit_size)) * self.fruit_size]

  def generate_new_fruit(self):
    self.fruit_pos = [random.randrange(1, (self.width // self.fruit_size)) * self.fruit_size,
                      random.randrange(1, (self.height // self.fruit_size)) * self.fruit_size]

class PoisonFruit:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.fruit_size = 10
    self.fruit_color = (255, 0, 0)
    self.fruit_pos = []

  def generate_new_fruit(self):
    self.fruit_pos = [random.randrange(1, (self.width // self.fruit_size)) * self.fruit_size,
                      random.randrange(1, (self.height // self.fruit_size)) * self.fruit_size]
