#SUDOKU SOLVER PROBLEM - given a sudoku board, find all the solutions
import random

'''This is board example from newspapers'''
board=[[0,0,2,0,0,0,9,1,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,5,1,0,0,3,0],
       [0,0,0,0,4,1,5,0,0],
       [0,0,8,7,0,9,1,0,0],
       [0,0,7,3,8,0,0,0,0],
       [0,2,3,0,0,8,4,7,0],
       [0,0,0,0,0,0,0,0,0],
       [0,4,1,0,0,0,8,9,0]]
#board=[[0 for x in range(9)] for y in range(9)]
#printBoard(board) - function that prints the board in an elegant way
def printBoard(board):
    print("-------------------")
    for y in range(len(board)):
        print("|",end="")
        for x in range(len(board[0])):
            print(board[y][x],end="|")
        print()
        print("-------------------")
    print("\n\n\n\n\n")
#solutions- list to hold all the solutions to the given puzzle
solutions=[]

#checkValid(x,y,n,board) - check if you could put number n at the position (x,y)
def checkValid(x,y,n,board):
    column = [board[i][x] for i in range(9)]
    row = board[y]
    if n in column:
        return False
    if n in row:
        return False
    quadrant_x=x//3
    pos_x=x%3
    quadrant_y=y//3
    pos_y=y%3
    for i in range(3):
        for k in range(3):
            if board[quadrant_y*3+i][quadrant_x*3+k]==n:
                return False
    return True

#solve(board,x=0,y=0) - main function that runs the aplication
def solve(board,x=0,y=0):
    if y>=len(board):
        y=0
        x+=1
    if x>=len(board[0]):
        printBoard(board.copy())
        return
    for i in range(1,10):
        if checkValid(x,y,i,board):
            board[y][x]=i
            solve(board,x,y+1)
            board[y][x]=0
    return
solve(board)