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
    
def counter(sudoku):
    num = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                num += 1
    return num

def findNextNum(numInts):
    maxI = 0
    max = -100
    numNulls = 0
    size = 9
    for i in range(size):
        # print(numInts)
        if numInts[i] > max:
            max = numInts[i]
            maxI = i
        if numInts[i] == -1:
            numNulls += 1
    if numNulls == size:
        return -1
    return (maxI + 1)

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

def updateAllArrays(arr, mainArr, coordI, coordJ, value):
    arr[coordI][coordJ], mainArr[coordI][coordJ] = value, value
    replaceZeros(arr, value, coordI, coordJ)

def myAlg(sudoku):
    import numpy as np
    import parities as p
    numInts = np.empty(9, dtype=np.int8)
    for i in range(9): numInts[i] = 0
    numInts, numAddedTotal = initializeNumInts(sudoku, numInts), 0
    sudokuBase = np.copy(sudoku)
    numToComplete = findNextNum(numInts)
    if numToComplete == -1:
        numInts, numToComplete = initializeNumInts(sudoku, numInts), findNextNum(numInts)

    for i in range(9):
        numToComplete = findNextNum(numInts)
        numAddedThisIteration = p.blockingCheck(sudoku, numToComplete, sudokuBase, numInts)
        numAddedTotal += numAddedThisIteration
        replaceZeroesFull(sudoku, numToComplete)
        sudoku = removeNegatives(sudoku)
        
    print(numAddedTotal)
    return numAddedTotal