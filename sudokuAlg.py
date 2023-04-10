import numpy as np
import os
os.system('cls')
import copy
import time
import parities as p
import stack as s
    
def replaceZeroesFull(arr, value):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            replaceZeros(arr, value, i, j)
    return arr

def replaceZeros(arr, value, i, j):
    row = len(arr)
    col = len(arr[0])
    if arr[i][j] == value:
            for k in range(col):
                if arr[i][k] == 0:
                    arr[i][k] = -1
            for k in range(row):
                if arr[k][j] == 0:
                    arr[k][j] = -1
    return arr  

def removeNegatives(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if arr[i][j] == -1:
                arr[i][j] = 0
    return arr    


def initializeNumInts(sudokuM, numInts):
    # X = sudokuM[0].size # 4
    # Y = int(sudokuM.size / sudokuM[0].size) # 3
    X, Y = 9, 9
    # can implement using binary heap (we want max value first)
    for x in range(X):
        for y in range(Y):
            int = sudokuM[y, x]
            if int > 0:
                numInts[ int - 1 ] += 1  
                
    return numInts

def sudokuGuesser(grid, numGuesses):
    stack = []
    stack.append(grid)
    
    while len(stack) > 0 and numGuesses <= 0:
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
        numGuesses -= 1
    grid = stack.pop()
    print(grid)
    return grid
                
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

def updateAllArrays(arr, mainArr, coordI, coordJ, value):
    arr[coordI][coordJ], mainArr[coordI][coordJ] = value, value
    replaceZeros(arr, value, coordI, coordJ)

def counter(sudoku):
    num = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                num += 1
    return num
                   
           
def mainRuntime(sudokuM):
    start_time = time.time()
    sudokuUnModified, sudokuSavePoint = np.array(sudokuM, copy=True), np.array(sudokuM, copy=True)

    numInts = np.empty(9, dtype=np.int8)
    for i in range(9): numInts[i] = 0

    numInts, numOnBoardAtStart = initializeNumInts(sudokuM, numInts), counter(sudokuM)
    maxIterations, boardSolved, totalAdded, numIterations = 15000, False, 0, 0 

    # stack = []
    # stack.append(sudokuM)
    
    numNoWrites = 0
    thresholdForGuessing = 10
    failedParity = 0

    for i in range(maxIterations):
        numToComplete = findNextNum(numInts)
        if numToComplete == -1:
            numInts, numToComplete = initializeNumInts(sudokuM, numInts), findNextNum(numInts)

        sudokuTemp = np.array(sudokuM, copy=True)
        replaceZeroesFull(sudokuTemp, numToComplete)
        
        numAddedThisIteration = p.blockingCheck(sudokuTemp, numToComplete, sudokuM, numInts)
        
        totalAdded += numAddedThisIteration
        sudokuTemp = removeNegatives(sudokuTemp)

        if (numNoWrites > thresholdForGuessing):
            sudokuSavePoint = sudokuM
            bruh = sudokuGuesser(sudokuM, 81)
            print(bruh - sudokuUnModified)
            numNoWrites = 0
            # print(sudokuM)
        elif numAddedThisIteration == 0:
            numNoWrites += 1
        
        if (totalAdded + numOnBoardAtStart == 81): 
            numIterations, boardSolved = i, True
            break
        
        if (p.parityCheckFull(sudokuM) == False):
            sudokuM = sudokuSavePoint
            failedParity += 1
        numIterations += 1
        
        if (numIterations % (maxIterations / 3) == 0): 
            print("iterations: " + str(numIterations))
            print("failed parity: " + str(failedParity))

    if (not boardSolved): print("\nWas unable to solve. Gave up after " + str(numIterations) + " iterations. ")
    else: print("\nSuccess! Solved after " + str(numIterations) + " iterations. ")

    print(sudokuM)
    print("\nNumbers Added:")
    print(sudokuM - sudokuUnModified)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Ran in {elapsed_time*1000:.4f} milliseconds ({elapsed_time:.4f} seconds).")
    
    return sudokuM
