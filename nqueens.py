'''Nqueens problem is a classic backtracking example. Given the width of the chessboard n, and n queens,
output every combination of queen positions, such that no queen attacks another (ignore colors of the pieces)
n - width of the chessboard and number of queens to be placed
board - list which stores solution that is currently being proccessed in the list format, where list index is x coordinate on the board, 
and the value at that index is y coordinate
solutions - list that stores all of our solutions'''
n = 9
board = [None for _ in range(n)]
solutions = []

'''boardCheck(board, k, i) - function that checks if queen can be placed at (k,i) position
NOTE: queen can move diagonally, vertically, horizontally'''
def boardCheck(board, k, i):
    for j in range(k):
        if board[j]==i:
            return False
        if board[j]-j==i-k:
            return False
        if board[j]+j==i+k:
            return False
    return True


def solve(k, n, board):
    # if we reached the end, that means that we filled the board, so we got a valid solution
    if k >= n:
        '''NOTE: here, I was stuck for a bit, because I forgot that lists does not store objects, but reference to the object, so .copy() is neccessary'''
        solutions.append(board.copy())
        return
    #we check for every y coordinate in range n (because n is height of our chessboard), if queen can be placed there
    for i in range(n):
        if boardCheck(board, k, i):
            #if it can be placed, place a queen there, check for further columns, and then return to check if there are more valid positions in the current column
            board[k] = i
            solve(k+1, n, board)
            board[k] = None
            '''TIP: remember this, because it's classic backtracking pattern'''
    return


#Call to the function and printing solutions to the console
solve(0, n, board)
print(solutions)



'''In the next part, I use pygame to better illustrate'''
import pygame
import random
pygame.init()



screen=pygame.display.set_mode([500,500])
running=True
# We will choose random solution from the list
random_solution=random.choice(solutions)
# field_width - width of the field on the chessboard
field_width=400//n

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #if we click on x, exit the loop
            running=False
    #fill the screen with white
    screen.fill((255, 255, 255))
    for i in range(n):
        for k in range(n):
            #this part is just to make sure we get black and white fields
            if (i+k)%2==0:
                color=(35,0,0)
            else:
                color=(191, 229, 216)
            # actually drawing the fields
            pygame.draw.rect(screen,color,pygame.Rect(50+i*field_width,50+k*field_width,field_width,field_width))
    for i in range(n):
        # drawing the circles( queens)
        pygame.draw.circle(screen,(0,0,0),(50+i*field_width+field_width//2,50+random_solution[i]*field_width+field_width//2),field_width//2-field_width//10)
    pygame.display.flip()
pygame.quit()