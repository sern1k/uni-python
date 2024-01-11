import sys
import numpy as np
from game_logic import is_terminal_node, winning_move, score_position, get_valid_locations, get_next_open_row, drop_piece
from constants import PLAYER_1_PIECE, PLAYER_2_PIECE

def minimax(board, depth, alpha, beta, maximizing_player):
  valid_locations_list = get_valid_locations(board)
  is_terminal = is_terminal_node(board)

  if depth == 0 or is_terminal:
    if is_terminal:
      if winning_move(board, PLAYER_2_PIECE):
        return (None, 100000000000000) # Max score for PLAYER_2_PIECE
      elif winning_move(board, PLAYER_1_PIECE):
        return (None, -100000000000000) # Min score for PLAYER_1_PIECE
      else:
        return (None, 0) # Draw
    else:
      return (None, score_position(board, PLAYER_2_PIECE))

  if maximizing_player:
    value = -sys.maxsize # Initialize value to negative infinity
    column = np.random.choice(valid_locations_list)

    # Iterate through valid columns and calculate scores
    for col in valid_locations_list:
      row = get_next_open_row(board, col)
      b_copy = board.copy()
      drop_piece(b_copy, row, col, PLAYER_2_PIECE)
      new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]

      if new_score > value:
        value = new_score
        column = col

      alpha = max(alpha, value)

      if alpha >= beta:
        break

    return column, value

  else:
    value = sys.maxsize
    column = np.random.choice(valid_locations_list)

    for col in valid_locations_list:
      row = get_next_open_row(board, col)
      b_copy = board.copy()
      drop_piece(b_copy, row, col, PLAYER_1_PIECE)
      new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]

      if new_score < value:
        value = new_score
        column = col

      beta = min(beta, value)

      if alpha >= beta:
        break

    return column, value
