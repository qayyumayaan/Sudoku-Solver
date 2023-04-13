import random

def generate_sudoku(difficulty):
    # Define the board dimensions
    board_size = 9
    box_size = 3
    
    # Initialize the empty board
    board = [[0 for x in range(board_size)] for y in range(board_size)]
    
    # Fill the board with random values
    for i in range(board_size):
        for j in range(board_size):
            # Determine the values for the current cell
            possible_values = list(range(1, board_size+1))
            random.shuffle(possible_values)
            
            # Check the rows, columns, and boxes to ensure no conflicts
            for value in possible_values:
                if (value not in board[i] and
                    value not in [board[k][j] for k in range(board_size)] and
                    value not in [board[m][n] for m in range(i//box_size*box_size, (i//box_size+1)*box_size) for n in range(j//box_size*box_size, (j//box_size+1)*box_size)]):
                    board[i][j] = value
                    break
    
    # Remove some values from the board to create a puzzle
    num_cells = difficulty * 10
    while num_cells > 0:
        i = random.randint(0, board_size-1)
        j = random.randint(0, board_size-1)
        if board[i][j] != 0:
            board[i][j] = 0
            num_cells -= 1
    
    return board

# print(generate_sudoku(3))

item = [
 [3, 0, 5, 9, 0, 8, 4, 6, 0], 
 [2, 0, 6, 0, 0, 0, 8, 0, 7], 
 [7, 0, 8, 6, 0, 0, 5, 0, 0], 
 [0, 8, 0, 3, 9, 0, 0, 7, 0], 
 [1, 3, 9, 8, 0, 0, 2, 0, 0], 
 [6, 2, 7, 1, 0, 0, 9, 4, 8], 
 [9, 0, 3, 0, 1, 0, 6, 0, 5], 
 [0, 0, 1, 4, 0, 0, 3, 2, 0], 
 [0, 5, 0, 0, 8, 9, 7, 1, 0]]

import sudokuAlg as sud
