def findEmptyLocation(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def isValid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num:
            return False
        if grid[i][col] == num:
            return False
        if grid[(row//3)*3 + i//3][(col//3)*3 + i%3] == num:
            return False
    return True

def solve(grid):
    emptyLoc = findEmptyLocation(grid)
    if not emptyLoc:
        return True
    row, col = emptyLoc
    for num in range(1, 10):
        if isValid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0
    return False


# if solve(grid):
#     for row in grid:
#         print(row)
# else:
#     print("No solution exists.")