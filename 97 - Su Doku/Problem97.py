# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:00:12 2022

@author: baran

Problem 97 - Su Doku
Simple Brute Force solver
"""

#Returns True if the entry sudoku[x,y] satisfies local necessary constraints,
#i.e. if sudoku[x,y] is not a duplicate within its quadrant and column and row
def CheckEntry(sudoku, x, y):
    #Scan col
    for i in range(9):
        if (sudoku[y][i] == sudoku[y][x] != 0) and (i != x):
            return False
    #Scan row
    for i in range(9):
        if (sudoku[i][x] == sudoku[y][x] != 0) and (i != y):
            return False
    #Scan quadrant
    for i in range(3 * (x//3), 3 * (x//3) + 3):
        for j in range(3 * (y//3), 3* (y//3) + 3):
            if (sudoku[j][i] == sudoku[y][x] != 0) and ((i != x) or (j != y)):
                return False
    return True

#Recursively brute force the sudoku grid, starting from the top left (0,0) and moving to the right & down, ending at (8,8)
#For each set position, the next position (x+1,y) is only looked at if (x,y) satisfies local constraints
def SolveSudoku(sudoku, x, y):
    if (y > 8):
        return True
    if (sudoku[y][x] == 0):
        #The (x,y) position is not set, hence iterate over 0..9
        for n in range(1,10):
            sudoku[y][x] = n
            if CheckEntry(sudoku,x,y):
                #The entry is locally valid, hence resume recursively with next field to the right (resp. down on the left)
                if SolveSudoku(sudoku, (x+1) % 9, y + (x+1)//9):
                    return True
        sudoku[y][x] = 0
        #If we end up here, then no entry at (x,y) is locally valid, i.e. a prior entry is incorrect (or the Sudoku is unsolvable)
        return False
    else:
        #The (x,y) position is already set, hence resume recursively with the next field to the right (resp. down on the left)
        return SolveSudoku(sudoku, (x+1) % 9, y + (x+1)//9)

file1 = open('p096_sudoku.txt', 'r')
lines = file1.readlines()

threeDigitSum = 0
for i in range(len(lines)):
    if (lines[i][:4] == "Grid"):
        #Next 9 lines after i represent a Sudoku grid
        sudoku = []
        for j in range(1,10):
            #Read line i+j
            sudoku.append([])
            for k in range(len(lines[i+j])):
                #Scan digit-by-digit from column k
                if (lines[i+j][k].isnumeric()):
                    sudoku[j-1].append(int(lines[i+j][k]))
        print("Unsolved & Solved Sudoku: ")
        print(sudoku)
        SolveSudoku(sudoku, 0, 0)
        print(sudoku)
        threeDigitSum += int(str(sudoku[0][0]) + str(sudoku[0][1]) + str(sudoku[0][2]))

print("Sum of digits is: {n}".format(n = threeDigitSum))