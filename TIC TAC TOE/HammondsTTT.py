#hunter helped me make make my bonus strategy

#import statements
import random as r
import os
########X

###############################################
gameBoard = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]

def printBoard(board):
    for i in range(3):
        print(f"{board[i][0]}|{board[i][1]}|{board[i][2]}")
        if(i != 2):
            print("-"*5)
    print()

def userTurn(sym,gameBoard):
    goodSpot = False    #takenspot will determine if valid input and spot taken
    while not goodSpot:  
        row = (int(input("enter a row: \n"))-1)
        col = (int(input("enter a column: \n"))-1)
        if row in range(3) and col in range(3):
            if takenSpot(sym,gameBoard,row,col):
                print("Spot Taken")
            else:
                goodSpot = True

# spot taken function
def takenSpot(sym,board,row,col):
    if board[row][col] == " ":
        board[row][col]=sym
        return False
    return True


def checkWinner(board):
    #horiz
    for r in range(len(board)):
        #r variable is for r
        if(board[r][0]==board[r][1] and board[r][1]==board[r][2] and board[r][0]==board[r][2] and board[r][0]!=" "):
            printBoard(board)
            return True
    #vert
    for c in range(len(board)):
        #r is the variable for which column its on
        if(board[0][c]==board[1][c] and board[1][c]==board[2][c] and board[0][c]==board[2][c] and board[0][c]!=" "):
            printBoard(board)
            return True
    #diag |||| specific spots for the 2 vert wins
        if(board[1][1]==board[0][0] and board[1][1]==board[2][2] and board[0][0]==board[2][2] and board[0][0]!=" ") or (board[1][1]==board[0][2] and board[1][1]==board[2][0] and board[0][2]==board[2][0] and board[0][2]!=" "):
            printBoard(board)
            return True
    return False




#########################
def tieCheck(board):
    #CAT or Tie or Scratch
    for row in board:
        if " " in row:
            return False
    printBoard(board)
    return True












def winID(board):
    possible,win,block = 0,0,0 #variables for searching possible win, block, and guaranteed win
    #horiz wins
    for i in range(3): #range of each row
        if (board[i][0]==board[i][1] and board[i][0]!=" ") or (board[i][1]==board[i][2] and board[i][1]!=" ") or (board[i][0]==board[i][2] and board[i][0]!=" "):
            possible = 1 #win is possible
            if (board[i][0]==" ") and (board[i][0]!="X" or board[i][0]!="O"):
                if (board[i][1]=="O"): #look for blocks
                    win = 1
                    winroco = [True,i,0] # pos,row,col
                r = i
                c = 0
                block = 1
                blockroco = [True,r,c]
            elif (board[i][1]==" ") and (board[i][1]!="X" or board[i][1]!="O"):
                if (board[i][0]=="O"):
                    win = 1
                    winroco = [True,i,1]
                r = i
                block,c = 1,1
                blockroco = [True,r,c]
            elif (board[i][2]==" ") and (board[i][2]!="X" or board[i][2]!="O"):
                if (board[i][1]=="O"):
                    win = 1
                    winroco = [True,i,2]
                r = i
                c = 2
                block = 1
                blockroco = [True,r,c]
    #vertical wins
    for i in range(3): #in the range of each column
        if((board[0][i]==board[1][i] and board[0][i]!=" ") or (board[1][i]==board[2][i] and board[1][i]!=" ") or (board[0][i]==board[2][i] and board[0][i]!=" ")):
            possible = 1
            if (board[0][i]==" ") and (board[0][i]!="X" or board[0][i]!="O"):
                if (board[1][i]=="O"):
                    win = 1
                    winroco = [True,0,i]
                r = 0
                c = i
                block = 1
                blockroco = [True,r,c]
            elif ((board[1][i]==" ") and (board[1][i]!="X" or board[1][i]!="O")):
                if (board[0][i]=="O"):
                    win = 1
                    winroco = [True,1,i]
                c = i
                block,r = 1,1
                blockroco = [True,r,c]
            elif ((board[2][i]==" ") and (board[2][i]!="X" or board[2][i]!="O")):
                if (board[1][i]=="O"):
                    win = 1
                    winroco = [True,2,i]
                r = 2
                c = i
                block = 1
                blockroco = [True,r,c]
    #diagonal wins
                #2 wins possible
    if((board[0][0]==board[1][1] and board[0][0]!=" ") or (board[1][1]==board[2][2] and board[1][1]!=" ") or (board[0][0]==board[2][2] and board[0][0]!=" ")):
        possible = 1
        if (board[0][0]==" ") and (board[0][0]!="X" or board[0][0]!="O"):
            if (board[1][1]=="O"):
                win = 1
                winroco = [True,0,0]
            r,c = 0,0
            block = 1
            blockroco = [True,r,c]
        elif (board[1][1]==" ") and (board[1][1]!="X" or board[1][1]!="O"):
            if (board[0][0]=="O"):
                win = 1
                winroco = [True,1,1]
            r,c,block = 1,1,1
            blockroco = [True,r,c]
        elif (board[2][2]==" ") and (board[2][2]!="X" or board[2][2]!="O"):
            if (board[1][1]=="O"):
                win = 1
                winroco = [True,2,2]
            r,c=2,2
            block = 1
            blockroco = [True,r,c]
    if((board[0][2]==board[1][1] and board[0][2]!=" ") or (board[1][1]==board[2][0] and board[2][0]!=" ") or (board[2][0]==board[0][2] and board[2][0]!=" ")):
        possible = 1
        if (board[0][2]==" ") and (board[0][2]!="X" or board[0][2]!="O"):
            if (board[1][1]=="O"):
                win = 1
                winroco = [True,0,2]
            r = 0
            c = 2
            block = 1
            blockroco = [True,r,c]
        elif (board[1][1]==" ") and (board[1][1]!="X" or board[1][1]!="O"):
            if (board[0][2]=="O"):
                win = 1
                winroco = [True,1,1]
            r,c,block=1,1,1
            blockroco = [True,r,c]
        elif (board[2][0]==" ") and (board[2][0]!="X" or board[2][0]!="O"):
            if (board[1][1]=="O"):
                win = 1
                winroco = [True,2,0]
            r = 2
            c = 0
            block = 1
            blockroco = [True,r,c]
    #differing between blocks and wins so that it can choose winning over a block
    if possible == 1:
        if win == 1:
            return winroco
        elif block == 1:
            return blockroco
    #if nothing is possible then it will basically just move on
    return [False]






def aiTurn(board):
    if winID(board)[0]==True:
        row = winID(board)[1]
        
        col = winID(board)[2]
    elif winID(board)[0]==False:
        row=r.randint(0,2)
        
        col=r.randint(0,2)
    return (row) , (col)

#user picks who goes first in game
sym = input("Is X or O Going First? (put it in caps)\n")
while(not(sym=="X" or sym=="O")):
    sym = input("Is X or O Going First? (put it in caps)\n")



print("Welcome to Tic-Tac-Toe!")
while(sym!="Q"):
    os.system("cls") #clear the screen
    #print the board
    printBoard(gameBoard)

    #checks if spot is taken and makes move if != taken
    if sym == "X":  #users's turn
        userTurn(sym,gameBoard)
    elif sym == "O":  #comp's turn
        goodSpot = False
        while not goodSpot:
            row,col = aiTurn(gameBoard)
            if takenSpot(sym,gameBoard,row,col):
                print("")
            else:
                  goodSpot = True
    
    os.system("cls")
    #############################
    #check for a winner
    if checkWinner(gameBoard) or tieCheck(gameBoard):
        winsym=sym 
        sym ="Q"

########################################################################

    if sym == "X":
        sym = "O"
        print("O's Turn")
    elif sym == "O":
        sym = "X"
        print("X's turn")
    os.system("cls")
if checkWinner(gameBoard):
    print(f"{winsym}'s Win!")
elif tieCheck(gameBoard):
    print("You Tied!")
    
    
    
    
    
    
    
    
    