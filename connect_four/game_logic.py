import numpy as np
import pygame
from constants import ROW_COUNT, COLUMN_COUNT, SQUARE_SIZE, RADIUS, PLAYER_1_PIECE, PLAYER_2_PIECE, EMPTY, BLUE, BLACK, RED, YELLOW, SIZE

def create_board():
  return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

def draw_board(board, screen):
  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT):
      pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
      pygame.draw.circle(screen, BLACK, (c * SQUARE_SIZE + SQUARE_SIZE // 2, (r+1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT):
      if board[r][c] == PLAYER_1_PIECE:
        pygame.draw.circle(screen, RED, (c * SQUARE_SIZE + SQUARE_SIZE // 2, SIZE[1] - r * SQUARE_SIZE - SQUARE_SIZE // 2), RADIUS)
      elif board[r][c] == PLAYER_2_PIECE:
        pygame.draw.circle(screen, YELLOW, (c * SQUARE_SIZE + SQUARE_SIZE // 2, SIZE[1] - r * SQUARE_SIZE - SQUARE_SIZE // 2), RADIUS)


def is_valid_location(board, col):
  return board[ROW_COUNT - 1][col] == EMPTY


def get_next_open_row(board, col):
  for row in range(ROW_COUNT):
    if board[row][col] == EMPTY:
      return row


def drop_piece(board, row, col, piece):
  board[row][col] = piece


def winning_move(board, piece):
  for r in range(ROW_COUNT):
    for c in range(COLUMN_COUNT - 3):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        return True

  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT - 3):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True

  for r in range(ROW_COUNT - 3):
    for c in range(COLUMN_COUNT - 3):
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        return True

  for r in range(3, ROW_COUNT):
    for c in range(COLUMN_COUNT - 3):
      if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
        return True

  return False

def get_valid_locations(board):
  valid_locations = []
  for col in range(COLUMN_COUNT):
    if is_valid_location(board, col):
      valid_locations.append(col)
  return valid_locations

def is_terminal_node(board):
  return winning_move(board, PLAYER_1_PIECE) or winning_move(board, PLAYER_2_PIECE) or len(get_valid_locations(board)) == 0

def score_position(board, piece):
  score = 0

  # Score center column
  center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
  center_count = center_array.count(piece)
  score += center_count * 3

  # Score horizontal
  for r in range(ROW_COUNT):
    row_array = [int(i) for i in list(board[r, :])]
    for c in range(COLUMN_COUNT - 3):
      window = row_array[c:c+4]
      score += evaluate_window(window, piece)

  # Score vertical
  for c in range(COLUMN_COUNT):
    col_array = [int(i) for i in list(board[:, c])]
    for r in range(ROW_COUNT - 3):
      window = col_array[r:r+4]
      score += evaluate_window(window, piece)

  # Score positive slope diagonals
  for r in range(ROW_COUNT - 3):
    for c in range(COLUMN_COUNT - 3):
      window = [board[r+i][c+i] for i in range(4)]
      score += evaluate_window(window, piece)

  # Score negative slope diagonals
  for r in range(ROW_COUNT - 3):
    for c in range(COLUMN_COUNT - 3):
      window = [board[r+3-i][c+i] for i in range(4)]
      score += evaluate_window(window, piece)

  return score

def evaluate_window(window, piece):
  score = 0
  opponent_piece = PLAYER_2_PIECE if piece == PLAYER_1_PIECE else PLAYER_1_PIECE

  if window.count(piece) == 4:
    score += 100
  elif window.count(piece) == 3 and window.count(EMPTY) == 1:
    score += 5
  elif window.count(piece) == 2 and window.count(EMPTY) == 2:
    score += 2

  if window.count(opponent_piece) == 3 and window.count(EMPTY) == 1:
    score -= 4

  return score
