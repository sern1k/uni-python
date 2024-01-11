import pygame
import sys
from game_logic import create_board, draw_board, is_valid_location, get_next_open_row, drop_piece, winning_move
from ai_logic import minimax
from constants import SIZE, SQUARE_SIZE, RADIUS, PLAYER_1_PIECE, PLAYER_2_PIECE, EMPTY, RED, YELLOW, BLACK, AI_LEVEL, ROW_COUNT, TEXT_PLACE

def main():
  pygame.init()
  board = create_board()
  game_over = False

  screen = pygame.display.set_mode(SIZE)
  pygame.display.set_caption("Connect Four")
  draw_board(board, screen)
  pygame.display.update()

  font = pygame.font.SysFont("Helvetica", 80)

  while not game_over:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      if event.type == pygame.MOUSEMOTION:
        pygame.draw.rect(screen, BLACK, (0, 0, SIZE[0], SQUARE_SIZE))
        posx = event.pos[0]
        if board[ROW_COUNT - 1][int(posx // SQUARE_SIZE)] == EMPTY:
          pygame.draw.circle(screen, RED, (int(posx), SQUARE_SIZE // 2), RADIUS)

      pygame.display.update()

      if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.rect(screen, BLACK, (0, 0, SIZE[0], SQUARE_SIZE))
        posx = event.pos[0]
        col = int(posx // SQUARE_SIZE)

        if is_valid_location(board, col):
          row = get_next_open_row(board, col)
          drop_piece(board, row, col, PLAYER_1_PIECE)

          if winning_move(board, PLAYER_1_PIECE):
            label = font.render("Player 1 wins!", 1, RED)
            screen.blit(label, TEXT_PLACE)
            game_over = True

          draw_board(board, screen)
          pygame.display.update()

          if not game_over:
            col, _ = minimax(board, AI_LEVEL, -sys.maxsize, sys.maxsize, True)
            pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_2_PIECE)

            if winning_move(board, PLAYER_2_PIECE):
              label = font.render("Player 2 wins!", 1, YELLOW)
              screen.blit(label, TEXT_PLACE)
              game_over = True

            draw_board(board, screen)
            pygame.display.update()

  pygame.time.wait(3000)

if __name__ == "__main__":
  main()
