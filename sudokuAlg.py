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
        
def makeAGuess(sudokuM, numInts):
    import random
    
    # for row in range(0 + randBlock % 3, 3 + randBlock % 3):
    #     for col in range(0 + randBlock % 3, 3 + randBlock % 3):
                  
    
    # guess = random.randint(1,9)
    # # for k in range(9):
    # #     for i in range((x // 3) * 3, 2 + (x // 3)):
    # #         for j in range((y // 3) * 3, 2 + (y // 3)):
    # #             if sudokuM[j][i] != k:
    # #                 guess = k
    # chosenX, chosenY = 0, 0
    
    # for x in range(9):
    #     for y in range(9):
    #         if sudokuM[y][x] == 0:
    #             for i in range(9):
    #                 if sudokuM[i][x] == guess:
    #                     break
    #                 if sudokuM[y][i] == guess:
    #                     break

    #             for i in range((x // 3) * 3, 2 + (x // 3)):
    #                 for j in range((y // 3) * 3, 2 + (y // 3)):
    #                     if sudokuM[j][i] == guess:
    #                         break
    #             chosenY = y
    #             chosenX = x
    #         break
    
    # sudokuM[chosenY][chosenX] = guess
    # item = Identifier(guess, y, x)
    # return item
    
    
    
    # print(sudokuM)
    # print(chosenX, chosenY)
    # x = random.randint(0,8)
    # y = random.randint(0,8)
    badGuess = False
    randBlock = random.randint(0,9)
    numInts = initializeNumInts(sudokuM, numInts)
    guess = findNextNum(numInts)
    randX = random.randint(0,8)
    randY = random.randint(0,8)
    print("making guess: ")
    while sudokuM[randY, randX] != 0:
        randX = random.randint(0,8)
        randY = random.randint(0,8)
        
        if sudokuM[randY][randX] == 0 & badGuess == False:
            
            for i in range(9):
                if sudokuM[i][randX] == guess:
                    badGuess == True
                    break
                if sudokuM[randY][i] == guess:
                    badGuess == True
                    break
            
            sudokuM[randY][randX] = guess
            
    item = Identifier(guess, randY, randX)
    return item




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
    for i in range(9):
        numInts[i] = 0
    numInts = initializeNumInts(sudokuM, numInts)
    # print(str(numInts))

    numOnBoardAtStart = counter(sudokuM)
    maxIterations, boardSolved, totalAdded, numIterations = 1500, False, 0, 0 
    
    # stack = 0
    stack = s.Stack(5)
    numNoWrites = 0
    thresholdUntilGuessing = 10
    thisSpotIsWrong = 0
    
    sudokuSavePoint = np.array(sudokuM, copy=True)

    for i in range(maxIterations):
        numToComplete = findNextNum(numInts)
        # print(str(numInts) + " num: " + str(numToComplete))
        if numToComplete == -1:
            numInts = initializeNumInts(sudokuM, numInts)
            numToComplete = findNextNum(numInts)
            # print(str(numInts) + " newNum: " + str(numToComplete))

        sudokuTemp = np.array(sudokuM, copy=True)
        replaceZeroesFull(sudokuTemp, numToComplete)
        
        numAddedThisIteration = p.blockingCheck(sudokuTemp, numToComplete, sudokuM, numInts)
        
        totalAdded += numAddedThisIteration
        
        if (numNoWrites > thresholdUntilGuessing):
            sudokuSavePoint = np.array(sudokuM, copy=True)
            stack.push(makeAGuess(sudokuM, numInts))
            numNoWrites = 0  
        elif numAddedThisIteration == 0:
            numNoWrites += 1
            
        sudokuTemp = removeNegatives(sudokuTemp)
        
        if (totalAdded + numOnBoardAtStart == 81): 
            numIterations = i
            boardSolved = True
            break
        
        if (p.parityCheckFull(sudokuM)):
            sudokuM = sudokuSavePoint
            if not stack.isEmpty():
                thisSpotIsWrong = stack.pop()
        numIterations += 1

    if (boardSolved == False): 
        print("Was unable to solve. Gave up after " + str(numIterations) + " iterations. ")
    else:
        print("Success! Solved after " + str(numIterations) + " iterations. ")

    p.parityCheckFull(sudokuM)

    print(sudokuM)
    print()
    print("Numbers Added:")
    print(sudokuM - sudokuUnModified)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Ran in {elapsed_time:.4f} seconds.")
    
    return sudokuM
