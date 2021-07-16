import pygame

from board import board

WIDTH = 550
HEIGHT = 550


def main():
    pygame.init()
    windows = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    windows.fill('white')
    bd = board(windows)
    for n in range(10):
        color = 'cadetblue2'
        width = 2
        pygame.draw.line(windows, color, (50, 50 + 50 * n), (500, 50 + 50 * n),width)
        pygame.draw.line(windows, color, (50 + 50 * n, 50), (50 + 50 * n, 500),width)
    for n in range(4):
        color = 'blue'
        width = 4
        pygame.draw.line(windows, color, (50, 50 + 150 * n), (500, 50 + 150 * n), width)
        pygame.draw.line(windows, color, (50 + 150 * n, 50), (50 + 150 * n, 500), width)
    for y,row in enumerate(bd.board):
        for x,value in enumerate(row):
            bd.draw_cell((0,0,0),x,y,bd.board[y][x])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bd.solve()


if __name__ == "__main__":
    main()
