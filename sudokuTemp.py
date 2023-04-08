import numpy as np

def find_empty_location(grid):
    """
    This function finds an empty location in the Sudoku grid.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def is_valid_number(grid, row, col, num):
    """
    This function checks if a given number is valid for a given cell in the Sudoku grid.
    """
    for i in range(9):
        if grid[row][i] == num:
            return False
        if grid[i][col] == num:
            return False
        if grid[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(grid):
    """
    This function solves the Sudoku puzzle using a recursive backtracking algorithm.
    """
    find = find_empty_location(grid)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid_number(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

# Example usage:
# grid = [
#     [3, 0, 6, 5, 0, 8, 4, 0, 0],
#     [5, 2, 0, 0, 0, 0, 0, 0, 0],
#     [0, 8, 7, 0, 0, 0, 0, 3, 1],
#     [0, 0, 3, 0, 0, 0, 0, 2, 0],
#     [9, 0, 0, 8, 0, 0, 0, 0, 5],
#     [0, 5, 0, 0, 0, 0, 6, 0, 0],
#     [1, 3, 0, 0, 0, 0, 2, 5, 0],
#     [0, 0, 0, 0, 0, 0, 0, 7, 4],
#     [0, 0, 5, 2, 0, 6, 3, 0, 0]
# ]

# grid = np.array([
#     [0, 0, 5,  3, 6, 0,  4, 0, 0],
#     [9, 6, 2,  0, 0, 4,  0, 7, 0],
#     [3, 0, 4,  0, 2, 9,  0, 6, 0],
    
#     [8, 2, 0,  9, 4, 0,  0, 1, 3],
#     [0, 4, 9,  0, 3, 0,  0, 5, 7],
#     [0, 0, 0,  2, 0, 0,  9, 8, 0],

#     [4, 0, 6,  0, 0, 1,  0, 0, 2],
#     [0, 0, 0,  6, 9, 3,  0, 0, 5],
#     [0, 0, 3,  0, 8, 0,  0, 0, 0]])


grid = np.array([ # 17 clue
    [0, 0, 0,  8, 0, 1,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 4, 3],
    [5, 0, 0,  0, 0, 0,  0, 0, 0],
    
    [0, 0, 0,  9, 7, 0,  8, 0, 0],
    [0, 0, 0,  0, 0, 0,  1, 0, 0],
    [0, 2, 0,  0, 3, 0,  0, 0, 0],

    [6, 0, 0,  0, 0, 0,  0, 7, 5],
    [0, 0, 3,  4, 0, 0,  0, 0, 0],
    [0, 0, 0,  2, 0, 0,  6, 0, 0]])

if solve_sudoku(grid):
    for row in grid:
        print(row)
else:
    print("No solution exists")