import numpy as np
import os
os.system('cls')
import copy
import time
import parities as p
import stack as s
    



def sudokuGuesser(grid, numGuesses):
    # print()
    # print(grid)
    stack = []
    gridBase = np.copy(grid)
    stack.append(grid)
    updated = False
    noValidSpotFound = True
    
    while len(stack) >= 1 and numGuesses >= 0:
        curr_grid = stack.pop()
        empty_cell = find_empty_location(curr_grid)
        if empty_cell is None:
            return curr_grid
        
        row, col = empty_cell
        
        seen_numbers = set()
        for token in range(1, 10):
            num = generate_new_number(seen_numbers)
            if is_valid_number(curr_grid, row, col, num):
                # new_grid = [row[:] for row in curr_grid]
                new_grid = np.copy(curr_grid)
                # print(new_grid)
                new_grid[row][col] = num
                stack.append(new_grid)
                updated = True
                noValidSpotFound = False
                break
        if updated == False:
            stack.append(curr_grid)
        elif updated == True:
            updated = False
        if noValidSpotFound:
            grid = gridBase

            
        numGuesses -= 1
    grid = stack.pop()
    # print(grid - gridBase)
    return grid


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


def generate_new_number(seen_numbers):
    import random
    while True:
        number = random.randint(1, 9)
        if number not in seen_numbers:
            seen_numbers.add(number)
            return number
                
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
    
def findNextNum(numInts):
    maxI = 0
    max = -100
    numNulls = 0
    size = 9
    for i in range(size):
        if numInts[i] > max:
            max = numInts[i]
            maxI = i
        if numInts[i] == -1:
            numNulls += 1
    if numNulls == size:
        return -1
    return (maxI + 1)
    
    # can implement using binary heap (we want max value first)
    # print(numInts) # gives # of integers present: [2 5 6 6 3 5 2 3 6 0]
    # print("frequency: " + str(freq) + " num: " + str(numToComplete))


                   
           
def mainRuntime(sudokuM):
    start_time = time.time()
    sudokuUnModified, sudokuSavePoint = np.array(sudokuM, copy=True), np.array(sudokuM, copy=True)

    numInts = np.empty(9, dtype=np.int8)
    for i in range(9): numInts[i] = 0

    # numInts, numOnBoardAtStart = initializeNumInts(sudokuM, numInts), counter(sudokuM)
    maxIterations, boardSolved, totalAdded, numIterations = 15000, False, 0, 0 

    stack = []
    stack.append(sudokuM)
    
    numNoWrites = 0
    thresholdForGuessing = 10
    failedParity = 0

    import myGoodAlg

    numOnBoardAtStart = myGoodAlg.counter(sudokuM)
    print(numOnBoardAtStart)
    
    for i in range(maxIterations):
        
        numAddedThisIteration = myGoodAlg.myAlg(sudokuM)
        totalAdded += numAddedThisIteration
        print(totalAdded)

        # if (numNoWrites > thresholdForGuessing):
        #     sudokuSavePoint = sudokuM
        #     # sudokuM = sudokuGuesser(sudokuM, 81)

        #     # print(bruh - sudokuUnModified)
        #     numNoWrites = 0
        #     # print(sudokuM)
        # elif numAddedThisIteration == 0:
        #     numNoWrites += 1
        
        if (totalAdded + numOnBoardAtStart == 81): 
            numIterations, boardSolved = i, True
            break
        
        # if (p.parityCheckFull(sudokuM) == False):
        #     sudokuM = sudokuSavePoint
        #     failedParity += 1
        #     print("failed")
        # numIterations += 1
        
        # if (numIterations % (maxIterations / 3) == 0): 
        #     print("iterations: " + str(numIterations))
        #     print("failed parity: " + str(failedParity))

    if (not boardSolved): print("\nWas unable to solve. Gave up after " + str(numIterations) + " iterations. ")
    else: print("\nSuccess! Solved after " + str(numIterations) + " iterations. ")

    print(sudokuM)
    print("\nNumbers Added:")
    print(sudokuM - sudokuUnModified)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Ran in {elapsed_time*1000:.4f} milliseconds ({elapsed_time:.4f} seconds).")
    
    return sudokuM
