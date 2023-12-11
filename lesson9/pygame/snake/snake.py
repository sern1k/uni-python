class Snake:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.snake_block = 10
    self.snake_speed = 15
    self.snake_length = 1
    self.snake_list = []
    self.snake_head = [width / 2, height / 2]

  def move(self, direction):
    if direction == "LEFT":
      self.snake_head[0] -= self.snake_block
    elif direction == "RIGHT":
      self.snake_head[0] += self.snake_block
    elif direction == "UP":
      self.snake_head[1] -= self.snake_block
    elif direction == "DOWN":
      self.snake_head[1] += self.snake_block

    self.snake_list.append(list(self.snake_head))
    if len(self.snake_list) > self.snake_length:
      del self.snake_list[0]
