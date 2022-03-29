import numpy as np 
import pygame
import math

rows =3 
columns = 3

width = 600 
length = 600 
windowSize = (600 , 600 )

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

circle = pygame.image.load('circle.png')
cross = pygame.image.load('x.png')

board = np.zeros((rows , columns ))

def mark (row , column , player ):
    board[row][column] = player
    
def isEmpty (row , column ):
    return board[row][column] == 0

def winningMove(player) :
    if (player == 1):
        winningColour = red
    else :
        winningColour = blue
        
    for r in range(rows):
        if (board[r][0] == player and board[r][1] == player and board[r][2] == player):
            pygame.draw.line(window , winnigColour , (10 , (r*200) + 100 ),(width-10 , (r*200)+100) , 10)
            return True
    for c in range(columns) :
        if (board[0][c] == player and board[1][c] == player and board[2][c] == player):
            pygame.draw.line(window , winningColour , ((c*200) +100 , 10) , ((c*200)+100 , length-10) , 10)
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        pygame.draw.line(window , winningColour , (10,10) , (590 , 590) , 10)
        return True
    if (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        pygame.draw.line(window , winningColour , (590,10) , (10 , 590) , 10)
        return True

def boardFull() :
    for i in range(rows):
        for j in range(columns):
            if (board[i][j] == 0 ):
                return False
    return True
def drawlines():
    pygame.draw.line(window,black,(200,0),(200,600),10)
    pygame.draw.line(window,black,(400,0),(400,600),10)
    pygame.draw.line(window,black,(0,200),(600,200),10)
    pygame.draw.line(window,black,(0,400),(600,400),10)

def drawBoard ():
    for c in range(columns):
        for r in range(rows):
            if (board[r][c] == 1):
                window.blit(cross , ((c*200)+50,(r*200)+50))
            if (board[r][c] == 2):
                window.blit(circle , ((c*200)+50,(r*200)+50))
    pygame.display.update()

endGame = False 
turn = 0

pygame.init()
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Tic Tac Toe")
window.fill(white)
drawlines()
pygame.display.update()


while (endGame == False ):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if (turn %2 == 0 ):
                print("player 1 :")
                row = math.floor(event.pos[1] / 200)
                column = math.floor(event.pos[0] / 200) 
                if (isEmpty(row , column)):
                    mark(row , column , 1)
                    if (winningMove(1) == True ):
                        endGame = True
                else:
                    turn-=1
            else :
                print("player 2 :")
                row = math.floor(event.pos[1] / 200)
                column = math.floor(event.pos[0] / 200)
                if (isEmpty(row , column)):
                    mark(row , column ,2)
                    if (winningMove(2) == True ):
                        endGame = True
                else:
                    turn-=1
                
            turn += 1
            print(board)
            drawBoard()
    if (boardFull() == True):
        endGame = True
                             
    if (endGame == True):
        pygame.time.wait(2000)
        board.fill(0)
        window.fill(white)
        drawlines()
        drawBoard()
        endGame = False
        pygame.display.update()
