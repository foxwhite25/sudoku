#include <stdio.h>
#include <time.h>

void printBoard(int board[9][9]) {
    for (int i = 0; i < 9; i++) {
        if (i % 3 == 0) printf(" =========================\n");
        for (int j = 0; j < 9; j++)
            j % 3 == 0 ? printf(" | %d", board[i][j]) : printf(" %d", board[i][j]);
        printf(" | \n");
    }
    printf(" =========================\n");
}


int isValid(int board[9][9], int x, int y, int value) {
    // Check row
    for (int i = 0; i <= 8; i++) {
        if (board[y][i] == value) return 0;
    }

    // Check collum
    for (int i = 0; i <= 8; i++) {
        if (board[i][x] == value) return 0;
    }

    // Check block
    int block_x = x - x % 3;
    int block_y = y - y % 3;
    for (int i = block_x; i < 3; i++) {
        for (int j = block_y; j < 3; j++) {
            if (board[j][i] == value) return 0;
        }
    }

    return 1;
}


int solve(int board[9][9], int x, int y) {
    if (x == 9 && y == 8) return 1;
    if (x == 9) {
        x = 0;
        y++;
    }
    if (board[y][x] > 0) return solve(board, x + 1, y);
    for (int value = 1; value <= 9; value++) {
        if (isValid(board, x, y, value) == 1) {
            board[y][x] = value;
            if (solve(board, x + 1, y) == 1) return 1;
            board[y][x] = 0;
        }
    }
    return 0;
}


int main() {
    clock_t start, end;
    double cpu_time_used;
    int board[9][9] = {
            {0, 0, 0, 0, 0, 0, 9, 0, 0},
            {0, 2, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 7, 0, 0, 0, 0},
            {0, 0, 0, 0, 3, 0, 0, 0, 0},
            {3, 0, 0, 0, 0, 7, 0, 0, 5},
            {0, 0, 0, 0, 0, 0, 3, 4, 6},
            {0, 0, 1, 2, 0, 0, 0, 0, 7},
            {6, 5, 0, 9, 8, 1, 4, 0, 2},
            {0, 8, 0, 0, 0, 3, 6, 5, 0},
    };
    start = clock();
    solve(board, 0, 0) == 1 ? printBoard(board) : printf("Invalid");
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("%f", cpu_time_used);
    return 0;
}
