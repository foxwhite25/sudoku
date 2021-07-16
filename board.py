import copy

import pygame


class board:
    def __init__(self,windows):
        self.windows = windows
        self.font = pygame.font.SysFont('Comic Sans MS',35)
        self.board = [[0, 8, 0, 4, 0, 0, 0, 6, 0],
                      [0, 2, 0, 0, 0, 0, 3, 5, 9],
                      [0, 0, 3, 0, 0, 2, 0, 0, 0],
                      [8, 0, 5, 0, 6, 0, 0, 0, 0],
                      [0, 0, 0, 7, 0, 3, 0, 0, 0],
                      [0, 0, 0, 0, 9, 0, 6, 0, 1],
                      [0, 0, 0, 3, 0, 0, 1, 0, 0],
                      [3, 5, 6, 0, 0, 0, 0, 4, 0],
                      [0, 4, 0, 0, 0, 9, 0, 2, 0]]

    def draw_cell(self,color,x,y,value):
        if not value:
            value = ' '
        word = self.font.render(str(value), False, color)
        pygame.draw.rect(self.windows,'white',((x * 50 + 55), (y * 50 + 55),40,40))
        self.windows.blit(word, ((x * 50 + 65), (y * 50 + 50)))
        pygame.display.update()

    def print_board(self):
        for row in self.board:
            print(row)
        print('=================================================')

    def is_valid(self, value, x, y):
        block_x, block_y = int(x / 3), int(y / 3)
        for idx, row in enumerate(self.board):
            if int(idx / 3) == block_y:
                for idx_2, cell in enumerate(row):
                    if int(idx_2 / 3) == block_x and cell == value:
                        return False
            if idx == y:
                for cell in row:
                    if cell == value:
                        return False
            if row[x] == value:
                return False
        return True

    def loop(self,x,y,bt):
        if bt:
            color1 = (255, 0, 0)
        else:
            color1 = (0,255,0)
        for num in range(1, 10):
            if self.board[y][x] + num < 10:
                if self.is_valid(self.board[y][x] + num,x, y):
                    self.board[y][x] += num
                    self.draw_cell(color1, x, y, self.board[y][x])
                    break
        else:
            return False
        return True

    def solve(self):
        cursor_x, cursor_y = 0, 0
        temp = copy.deepcopy(self.board)
        backtrack = False
        while True:
            while not backtrack:
                if cursor_x == 9:
                    cursor_x = 0
                    cursor_y += 1
                    continue
                if cursor_y == 9:
                    return True
                if temp[cursor_y][cursor_x]:
                    cursor_x += 1
                    continue
                if self.loop(cursor_x,cursor_y,False):
                    cursor_x += 1
                else:
                    backtrack = True
            while backtrack:
                cursor_x -= 1
                if cursor_x == -1:
                    cursor_x = 9
                    cursor_y -= 1
                    continue
                if cursor_y == -1:
                    return False
                if temp[cursor_y][cursor_x]:
                    continue
                if not self.loop(cursor_x,cursor_y,True):
                    self.board[cursor_y][cursor_x] = 0
                    self.draw_cell((0,0,0),cursor_x,cursor_y,' ')
                    continue
                cursor_x += 1
                backtrack = False
