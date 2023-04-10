# def makeAGuess(sudokuM, numInts):
#     import random
    
#     # for row in range(0 + randBlock % 3, 3 + randBlock % 3):
#     #     for col in range(0 + randBlock % 3, 3 + randBlock % 3):
                  
    
#     # guess = random.randint(1,9)
#     # # for k in range(9):
#     # #     for i in range((x // 3) * 3, 2 + (x // 3)):
#     # #         for j in range((y // 3) * 3, 2 + (y // 3)):
#     # #             if sudokuM[j][i] != k:
#     # #                 guess = k
#     # chosenX, chosenY = 0, 0
    
#     # for x in range(9):
#     #     for y in range(9):
#     #         if sudokuM[y][x] == 0:
#     #             for i in range(9):
#     #                 if sudokuM[i][x] == guess:
#     #                     break
#     #                 if sudokuM[y][i] == guess:
#     #                     break

#     #             for i in range((x // 3) * 3, 2 + (x // 3)):
#     #                 for j in range((y // 3) * 3, 2 + (y // 3)):
#     #                     if sudokuM[j][i] == guess:
#     #                         break
#     #             chosenY = y
#     #             chosenX = x
#     #         break
    
#     # sudokuM[chosenY][chosenX] = guess
#     # item = Identifier(guess, y, x)
#     # return item
    
    
    
#     # print(sudokuM)
#     # print(chosenX, chosenY)
#     # x = random.randint(0,8)
#     # y = random.randint(0,8)
#     badGuess = False
#     randBlock = random.randint(0,9)
#     numInts = initializeNumInts(sudokuM, numInts)
#     guess = findNextNum(numInts)
#     randX = random.randint(0,8)
#     randY = random.randint(0,8)
#     print("making guess: ")
#     while sudokuM[randY, randX] != 0:
#         randX = random.randint(0,8)
#         randY = random.randint(0,8)
        
#         if sudokuM[randY][randX] == 0 & badGuess == False:
            
#             for i in range(9):
#                 if sudokuM[i][randX] == guess:
#                     badGuess == True
#                     break
#                 if sudokuM[randY][i] == guess:
#                     badGuess == True
#                     break
            
#             sudokuM[randY][randX] = guess
            
#     item = Identifier(guess, randY, randX)
#     return item