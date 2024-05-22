import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 5, 5
SQUARE_SIZE = WIDTH // BOARD_COLS


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")


def draw_board():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, WHITE, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, WHITE, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_symbols(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, WHITE, (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + 10),
                                 ((col + 1) * SQUARE_SIZE - 10, (row + 1) * SQUARE_SIZE - 10), LINE_WIDTH)
                pygame.draw.line(screen, WHITE, ((col + 1) * SQUARE_SIZE - 10, row * SQUARE_SIZE + 10),
                                 (col * SQUARE_SIZE + 10, (row + 1) * SQUARE_SIZE - 10), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10, LINE_WIDTH)


def check_winner(board, symbol):
    for row in range(BOARD_ROWS):
        if all(board[row][col] == symbol for col in range(BOARD_COLS)):
            return True
    for col in range(BOARD_COLS):
        if all(board[row][col] == symbol for row in range(BOARD_ROWS)):
            return True
    if all(board[i][i] == symbol for i in range(BOARD_ROWS)) or \
       all(board[i][BOARD_COLS-1-i] == symbol for i in range(BOARD_ROWS)):
        return True
    return False


def check_draw(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                return False
    return True


def make_pc_move(board, symbol):
    empty_cells = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] == ' ']
    return random.choice(empty_cells)


def main():
    board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    turn = 'X'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if turn == 'X' and event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE
                if board[row][col] == ' ':
                    board[row][col] = turn
                    if check_winner(board, turn):
                        print(f'{turn} победил!')
                        pygame.quit()
                        sys.exit()
                    elif check_draw(board):
                        print('Ничья!')
                        pygame.quit()
                        sys.exit()
                    turn = 'O'

            if turn == 'O':
                row, col = make_pc_move(board, turn)
                board[row][col] = turn
                if check_winner(board, turn):
                    print(f'{turn} победил!')
                    pygame.quit()
                    sys.exit()
                elif check_draw(board):
                    print('Ничья!')
                    pygame.quit()
                    sys.exit()
                turn = 'X'

        screen.fill(BLACK)
        draw_board()
        draw_symbols(board)
        pygame.display.flip()


if __name__ == '__main__':
    main()
