import numpy as np
import sudokuAlg as sud

def parityCheckFull(sudoku): # works on completed board
    rows = len(sudoku)
    cols = len(sudoku[0])
    # check = np.empty(9, dtype = np.int8)

    for rowNum in range(cols):
        errorCol = parityCheckCol(sudoku, rowNum)
    for colNum in range(rows):
        errorRow = parityCheckRow(sudoku, colNum)

    if errorCol == -1 or errorRow == -1:
        return True
    else:
        return False
                
def parityCheckCol(sudoku, rowNum):
    errorInCol = -1
    numInCheckBlock = 0
    check = np.empty(9, dtype = np.int8)
    for i in range(9):
        check[i] = 0
    for j in range(9):
        if sudoku[j][rowNum] > 0:
            check[sudoku[j][rowNum] - 1] += 1
            numInCheckBlock += 1
    
    if numInCheckBlock == 9:
        for k in range(9):
            if check[k] != 1:
                errorInCol = j
                break
    # if numInCheckBlock == 8:
    #     for k in range(9):
    #         if check[k] == 0:
    #             sudoku[j][rowNum] = k + 1
    #             errorInCol = -2
    #             break

    return errorInCol

def parityCheckRow(sudoku, colNum):
    errorInRow = -1
    numInCheckBlock = 0
    check = np.empty(9, dtype = np.int8)
    for i in range(9):
        check[i] = 0
    for i in range(9):
        if sudoku[colNum][i] > 0:
            check[sudoku[i][colNum] - 1] += 1
            numInCheckBlock += 1
            
    if numInCheckBlock == 9:
        for k in range(9):
            if check[k] != 1:
                errorInRow = i
                break
    # if numInCheckBlock == 8:
    #     for k in range(9):
    #         if check[k] == 0:
    #             sudoku[i][colNum] = k + 1
    #             errorInRow = -2
    #             break
            
    return errorInRow

def blockingCheck(arr, value, mainArr, numInts):

    coordI = 0
    coordJ = 0
    numUpdated = 0
    interval = 3
    row = len(arr)
    col = len(arr[0])
    for blockX in range(0,row,interval):
        for blockY in range(0, col, interval):
            numZeros = 0
            
            for i in range(blockX, blockX+interval):
                for j in range(blockY, blockY+interval):
                    # print(i,j)
                    if arr[i][j] == value:
                        numZeros = -100
                        break
                    if arr[i][j] == 0:
                        numZeros += 1
                        coordI = i
                        coordJ = j
                        
                if arr[i][j] == value:
                    numZeros = -100
                    break            
                        
            if numZeros == 1:
                import myGoodAlg
                myGoodAlg.updateAllArrays(arr, mainArr, coordI, coordJ, value)
                numUpdated += 1
    numInts[value - 1] = -1
    return numUpdated


