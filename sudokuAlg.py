import numpy as np
import os
os.system('cls')
import copy
import time
import parities as p
import stack as s

class Identifier:
    def __init__(self, num, row, col):
        self.num = num
        self.row = row
        self.col = col
        
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def getNum(self):
        return self.num
    
    def setRow(self, r):
        row = r
    def setCol(self, c):
        col = c
    def setNum(self, n):
        num = n
        

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
    maxIterations, boardSolved, totalAdded, numIterations = 1500, False, 0, 0 

    for i in range(maxIterations):
        numToComplete = findNextNum(numInts)
        if numToComplete == -1:
            numInts, numToComplete = initializeNumInts(sudokuM, numInts), findNextNum(numInts)

        sudokuTemp = np.array(sudokuM, copy=True)
        replaceZeroesFull(sudokuTemp, numToComplete)
        
        numAddedThisIteration = p.blockingCheck(sudokuTemp, numToComplete, sudokuM, numInts)
        
        totalAdded += numAddedThisIteration
        sudokuTemp = removeNegatives(sudokuTemp)
        
        if (totalAdded + numOnBoardAtStart == 81): 
            numIterations, boardSolved = i, True
            break
        
        if (p.parityCheckFull(sudokuM) == False):
            sudokuM = sudokuSavePoint
        numIterations += 1

    if (boardSolved == False): 
        print("\nWas unable to solve. Gave up after " + str(numIterations) + " iterations. ")
    else:
        print("\nSuccess! Solved after " + str(numIterations) + " iterations. ")

    p.parityCheckFull(sudokuM)

    print(sudokuM)
    print("\nNumbers Added:")
    print(sudokuM - sudokuUnModified)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Ran in {elapsed_time*1000:.4f} milliseconds ({elapsed_time:.4f} seconds).")
    
    return sudokuM
