import pygame
import sys
import numpy as np

# Ustawienia gry
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE // 2 - 5
PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2
EMPTY = 0

WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)

# Ustawienia kolorów
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

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
                pygame.draw.circle(screen, RED, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - r * SQUARE_SIZE - SQUARE_SIZE // 2), RADIUS)
            elif board[r][c] == PLAYER_2_PIECE:
                pygame.draw.circle(screen, YELLOW, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - r * SQUARE_SIZE - SQUARE_SIZE // 2), RADIUS)

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == EMPTY

def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == EMPTY:
            return row

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Sprawdź wiersze
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Sprawdź kolumny
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Sprawdź pozytywne nachylone przekątne
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Sprawdź negatywne nachylone przekątne
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

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

def score_position(board, piece):
    score = 0

    # Ocena środkowej kolumny
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Ocena pozioma
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Ocena pionowa
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Ocena pozytywnie nachylonych przekątnych
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Ocena negatywnie nachylonych przekątnych
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def is_terminal_node(board):
    return winning_move(board, PLAYER_1_PIECE) or winning_move(board, PLAYER_2_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizing_player):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, PLAYER_2_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_1_PIECE):
                return (None, -100000000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, PLAYER_2_PIECE))

    if maximizing_player:
        value = -sys.maxsize
        column = np.random.choice(valid_locations)

        for col in valid_locations:
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
        column = np.random.choice(valid_locations)

        for col in valid_locations:
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

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def main():
    pygame.init()
    board = create_board()
    game_over = False

    screen = pygame.display.set_mode(SIZE)
    draw_board(board, screen)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                posx = event.pos[0]
                if board[0][int(posx // SQUARE_SIZE)] == EMPTY:
                    pygame.draw.circle(screen, RED, (int(posx), SQUARE_SIZE // 2), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                posx = event.pos[0]
                col = int(posx // SQUARE_SIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_1_PIECE)

                    if winning_move(board, PLAYER_1_PIECE):
                        label = myfont.render("Player 1 wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

                    draw_board(board, screen)
                    pygame.display.update()

                    if not game_over:
                        # Komputer wykonuje ruch
                        col, _ = minimax(board, 5, -sys.maxsize, sys.maxsize, True)
                        pygame.time.wait(500)  # Czekaj chwilę przed ruchem komputera
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_2_PIECE)

                        if winning_move(board, PLAYER_2_PIECE):
                            label = myfont.render("Player 2 wins!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                        draw_board(board, screen)
                        pygame.display.update()

    pygame.time.wait(3000)  # Czekaj przed zamknięciem okna

if __name__ == "__main__":
    main()
