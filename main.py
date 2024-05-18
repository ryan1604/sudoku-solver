import os
from time import sleep

def is_valid(val, row, col, board):
    start_row = 3 * (row // 3) # get start row for 3x3 grid
    start_col = 3 * (col // 3) # get start col for 3x3 grid

    # check if val is in row
    if val in board[row]:
        return False
    
    # check if val is in column
    for values in board:
        if val == values[col]:
            return False
    
    # check if val is in 3x3 grid
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if val == board[i][j]:
                return False
            
    return True

def print_board(board):
    os.system("cls")
    for row in board:
        print(row)
    #sleep(0.1)

def solve(board):
    # start from first row and check each cell in the row
    for row, values in enumerate(board): # row = index, values = array of values
        for col, value in enumerate(values): # col = index, value = value at index in row array
            if value == "_":
                for i in range(1, 10):
                    if is_valid(str(i), row, col, board):
                        board[row][col] = str(i)
                        print_board(board)
                        if solve(board):
                            return True
                        board[row][col] = "_"
                        print_board(board)
                return False
    return True


def main():
    board = []
    print("Enter a 9x9 sudoku board:")
    for i in range(9):
        board.append(list(input()))
    
    if not solve(board):
        print("Sudoku has no solution!")   

if __name__ == "__main__":
    main()