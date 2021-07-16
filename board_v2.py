import time


class board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
                      [0, 2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 7, 0, 0, 0, 0],
                      [0, 0, 0, 0, 3, 0, 0, 0, 0],
                      [3, 0, 0, 0, 0, 7, 0, 0, 5],
                      [0, 0, 0, 0, 0, 0, 3, 4, 6],
                      [0, 0, 1, 2, 0, 0, 0, 0, 7],
                      [6, 5, 0, 9, 8, 1, 4, 0, 2],
                      [0, 8, 0, 0, 0, 3, 6, 5, 0]]

    def is_valid(self, pos, value):
        # Check row
        for cell in self.board[pos[1]]:
            if value == cell:
                return False

        # Check column
        for row in self.board:
            if row[pos[0]] == value:
                return False

        # Check block
        block_x, block_y = pos[0] // 3, pos[1] // 3
        for y in range(block_y * 3, block_y * 3 + 3):
            for x in range(block_x * 3, block_x * 3 + 3):
                if self.board[y][x] == value and (x,y) != pos:
                    return False
        return True

    def get_empty_cell(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    return x, y
        return None

    def solve(self):
        empty = self.get_empty_cell()
        if empty:
            x, y = empty
        else:
            return True
        for n in range(1, 10):
            if self.is_valid(empty, n):
                self.board[y][x] = n
                if self.solve():
                    return True
                self.board[y][x] = 0
        return False


bd = board()
start = time.time()
bd.solve()
print(bd.board)
print(f'Took {time.time()-start}s to solve the sudoku')
