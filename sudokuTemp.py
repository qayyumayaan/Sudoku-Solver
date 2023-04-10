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

def nakedSingleInSubArray(arr):
    num2update = -1
    col2update = -1
    numInAisle = 0
    parity = np.empty(9)
    for i in range(9):
        parity[i] = 0
        if (arr[i] != 0):
            parity[arr[i]] += 1
            numInAisle += 1
        else: 
            col2update = i
        
    if numInAisle == 8:
        for i in range(9):
            if parity[i] == 0:
                num2update = i
        arr[col2update] = num2update
        return True
    else:
        return False
    # grid[row][col2update] = num2update
        
def nakedSingle(grid):

    for i in range(9):
        subArray = np.array(9)
        for j in range(9):
            subArray[j] = grid[i][j]
        if not nakedSingleInSubArray(subArray):
            for j in range(9):
                grid[i][j] = subArray[j]
                
    for j in range(9):
        subArray = np.array(9)
        for i in range(9):
            subArray[i] = grid[i][j]
        if not nakedSingleInSubArray(subArray):
            for i in range(9):
                grid[i][j] = subArray[i]
    
            
        
        

                


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


def solve_sudoku_iteratively(grid):
    stack = []
    stack.append(grid)
    
    while len(stack) > 0:
        curr_grid = stack.pop()
        empty_cell = find_empty_location(curr_grid)
        if empty_cell is None:
            return curr_grid
        
        row, col = empty_cell
        for num in range(1, 10):
            if is_valid_number(curr_grid, row, col, num):
                new_grid = [row[:] for row in curr_grid]
                new_grid[row][col] = num
                stack.append(new_grid)
    
    return None


grid = np.array([
[	0	,	0	,	5	,	3	,	6	,	7	,	4	,	2	,	9	],
[	0	,	6	,	2	,	5	,	1	,	4	,	3	,	7	,	8	],
[	0	,	7	,	4	,	8	,	2	,	9	,	5	,	6	,	1	],
[	0	,	2	,	7	,	9	,	4	,	5	,	6	,	1	,	3	],
[	0	,	4	,	9	,	1	,	3	,	8	,	2	,	5	,	7	],
[	0	,	3	,	9	,	2	,	7	,	6	,	9	,	8	,	4	],
[	0	,	9	,	6	,	7	,	5	,	1	,	8	,	3	,	2	],
[	0	,	1	,	8	,	6	,	9	,	3	,	7	,	4	,	5	],
[	0	,	5	,	3	,	4	,	8	,	2	,	1	,	9	,	6	], ])



# if solve_sudoku_iteratively(grid):
#     for row in grid:
#         print(row)
# else:
#     print("No solution exists")
    
    
# print()

# if solve_sudoku(grid):
#     for row in grid:
#         print(row)
# else:
#     print("No solution exists")
    
    
grid = np.array([
[	0	,	0	,	5	,	3	,	6	,	7	,	4	,	2	,	9	],
[	0	,	6	,	2	,	5	,	1	,	4	,	3	,	7	,	8	],
[	0	,	7	,	4	,	8	,	2	,	9	,	5	,	6	,	1	],
[	0	,	2	,	7	,	9	,	4	,	5	,	6	,	1	,	3	],
[	0	,	4	,	9	,	1	,	3	,	8	,	2	,	5	,	7	],
[	0	,	3	,	9	,	2	,	7	,	6	,	9	,	8	,	4	],
[	0	,	9	,	6	,	7	,	5	,	1	,	8	,	3	,	2	],
[	0	,	1	,	8	,	6	,	9	,	3	,	7	,	4	,	5	],
[	0	,	5	,	3	,	4	,	8	,	2	,	1	,	9	,	6	], ])
    
print()
    
if nakedSingle(grid):
    for row in grid:
        print(row)
    
    
