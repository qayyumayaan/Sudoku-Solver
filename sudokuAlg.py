import numpy as np
import os
os.system('cls')
import copy
import time

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

def blockingCheck(arr, value, mainArr, numInts):
    interval = 3
    row = len(arr)
    col = len(arr[0])
    coordI = 0
    coordJ = 0
    numUpdated = 0
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
                updateAllArrays(arr, mainArr, coordI, coordJ, value)
                numUpdated += 1
    numInts[value - 1] = -1
    return numUpdated

def initializeNumInts(sudokuM, numInts):
    # X = sudokuM[0].size # 4
    # Y = int(sudokuM.size / sudokuM[0].size) # 3
    X, Y = 9, 9
    # can implement using binary heap (we want max value first)
    for x in range(X):
        for y in range(Y):
            int = sudokuM[y, x]
            if int != 0:
                numInts[ int - 1 ] += 1  
                
    return numInts
    
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
    arr[coordI][coordJ] = value
    mainArr[coordI][coordJ] = value
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
    sudokuUnModified = np.array(sudokuM, copy=True)

    numInts = np.empty(9, dtype=np.int8)
    numInts = initializeNumInts(sudokuM, numInts)
    # print(str(numInts))

    numOnBoardAtStart = counter(sudokuM)
    maxIterations, boardSolved, totalAdded, numIterations = 1500, False, 0, 0 

    for i in range(maxIterations):
        numToComplete = findNextNum(numInts)
        # print(str(numInts) + " num: " + str(numToComplete))
        if numToComplete == -1:
            numInts = initializeNumInts(sudokuM, numInts)
            numToComplete = findNextNum(numInts)
            # print(str(numInts) + " newNum: " + str(numToComplete))

        sudokuTemp = np.array(sudokuM, copy=True)
        replaceZeroesFull(sudokuTemp, numToComplete)
        totalAdded += blockingCheck(sudokuTemp, numToComplete, sudokuM, numInts)
        sudokuTemp = removeNegatives(sudokuTemp)
        
        if (totalAdded + numOnBoardAtStart == 81): 
            numIterations = i
            boardSolved = True
            break

    if (boardSolved == False): 
        print("Was unable to solve. Gave up after " + str(maxIterations) + " iterations. ")
    else:
        print("Success! Solved after " + str(numIterations) + " iterations. ")

    print(sudokuM)
    print()
    print("Numbers Added:")
    print(sudokuM - sudokuUnModified)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Ran in {elapsed_time:.4f} seconds.")
    
    return sudokuM