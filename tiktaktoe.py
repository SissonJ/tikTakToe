import numpy as np
import sys

def createGameBoard():
    gameboard = np.empty([11,11],dtype=object)
    counter = 1
    for i in range(11):
        #gameboard[i]=np.zeros(11)
        for j in range(11):
            gameboard[j,i]=' '
            if i==3 or i==7:
                gameboard[j,i]='-'
            if j==3 or j==7:
                gameboard[j,i]='|'
            if (j==1 or j==5 or j==9) and (i==1 or i==5 or i==9):
                gameboard[j,i]=counter
                counter = counter+1
    return gameboard

def printGameBoard(board):
    for i in range(11):
        for j in range(11):
            print(board[j,i],end =""),
        print('\n')

def isGameWon(board):
    col=1
    row=1
    trackerDiag =np.array( [board[1,1],board[1,9]])
    tracker = 0
    for i in range(3):
        col=1+i*4
        row=1+i*4
        if board[1,col]==board[5,col] and board[9,col]==board[5,col]:
            #print("Player", board[1,col], "has won the game!", sep=" ")
            return False
        elif board[row,1]==board[row,5] and board[row,9]==board[row,5]:
            #print("Player", board[row,1], "has won the game!", sep=" ")
            return False
        elif trackerDiag[0] == board[5,5] and board[9,9]==board[5,5]:
            #print("Player", board[5,5], "has won the game!", sep=" ")
            return False
        elif trackerDiag[1] == board[5,5] and board[5,5] == board[9,1]:
            #print("Player", board[5,5], "has won the game!", sep=" ")
            return False
        else:
            for i in range(11):
                for j in range(11):
                    
                    if board[j,i]=='O' or board[j,i]=='X':
                        tracker = tracker + 1
                        #print(tracker)
    if tracker == 27:
        return False
    return True

def whoWon(board):
    col=1
    row=1
    trackerDiag =np.array( [board[1,1],board[1,9]])
    tracker = 0
    catsGame='C'
    for i in range(3):
        col=1+i*4
        row=1+i*4
        if board[1,col]==board[5,col] and board[9,col]==board[5,col]:
            #print("Player", board[1,col], "has won the game!", sep=" ")
            return board[1,col]
        elif board[row,1]==board[row,5] and board[row,9]==board[row,5]:
            #print("Player", board[row,1], "has won the game!", sep=" ")
            return board[row,1]
        elif trackerDiag[0] == board[5,5] and board[9,9]==board[5,5]:
            #print("Player", board[5,5], "has won the game!", sep=" ")
            return board[5,5]
        elif trackerDiag[1] == board[5,5] and board[5,5] == board[9,1]:
            #print("Player", board[5,5], "has won the game!", sep=" ")
            return board[5,5]
        else:
            for i in range(11):
                for j in range(11):
                    if board[j,i]=='O' or board[j,i]=='X':
                        tracker = tracker+1
    if tracker == 27:
        return 0

                            
    return catsGame
        
def gameMove(board,player,move, isReset):
    dummy=0
    x=1
    y=1
    if not isReset:
        move = isMoveValid(board, move, False)
        for i in range(9):
            dummy=i+1
            if x>9:
                x=1
            else:
                pass
            if dummy==4 or dummy==7:
                y=y+4
            else:
                pass
            if move==dummy:
                if player:
                    #print('O')
                    board[x,y]='O'
                    break
                else:
                    #print('x')
                    board[x,y]='X'
                    break
            x=x+4
    else:
            
        for i in range(9):
            dummy=i+1
            if x>9:
                x=1
            else:
                pass
            if dummy==4 or dummy==7:
                y=y+4
            else:
                pass
            if move==dummy:
                board[x,y]=' '
        x=x+4
    return board

def isMoveValid(board, move, isBool):
    if not isBool:
        validMove=False
        x=1
        y=1
        dummy=1
        while not validMove:
           for i in range(9):
                dummy=i+1
                if x>9:
                    x=1
                else:
                    pass
                if dummy==4 or dummy==7:
                    y=y+4
                else:
                    pass
                if move==dummy:
                    if board[x,y]=='O' or board[x,y]=='X':
                        print("That move is not valid")
                        move = input("Please enter a new move (1-9): ")
                        move = int(move)
                        move = isMoveValid(board, move, False)
                    else:
                        validMove=True
                        break
                x=x+4
        return move
    else:
        validMove=False
        x=1
        y=1
        dummy=1
        while not validMove:
           for i in range(9):
                dummy=i+1
                if x>9:
                    x=1
                else:
                    pass
                if dummy==4 or dummy==7:
                    y=y+4
                else:
                    pass
                if move==dummy:
                    if board[x,y]=='O' or board[x,y]=='X':
                        return False
                    else:
                        validMove=True
                        return True
                x=x+4

def bestMove(board,isMax,maxDepth):
    score = 0
    hiScore = -1000000
    loScore = 1000000
    move = 0
    dumdum=0
    dumBoard = 0
    availMoves = np.array([])
    for i in range(9):
        dumdum=i+1
        if isMoveValid(board,dumdum,True):
            availMoves = np.append(availMoves, dumdum)
    if len(availMoves) == 9:
        return 9
    print(availMoves)
    dumMoves = np.copy(availMoves)
    for i in range(len(availMoves)):
        dumMoves = np.copy(availMoves)
        dumBoard = np.copy(board)
        dumBoard = gameMove(dumBoard, isMax, availMoves[i], False)
        dumMoves = np.delete(dumMoves, i)
        score = minimax(dumBoard,not isMax, 0, 0, 0, dumMoves)
        print(score)
        if isMax:
            if score >= hiScore:
                hiScore = score
                move = availMoves[i]
        else:
            if score <= loScore:
                loScore = score
                move = availMoves[i]
    
    return move
            



def minimax(board,isMax,h, currDepth,maxDepth,availMoves):
    #O wants to max, X wants to min
    dumdum=np.copy(availMoves)
    dumBoard = board
    hiScore = -1000000
    loScore = 10000000
    score = 0
    
    if whoWon(board)=='X':
        return -10+currDepth
    elif whoWon(board)=='O':
        return 10-currDepth
    elif whoWon(board)==0:
        return 0
    else:
        for i in range(len(availMoves)):
            dumdum = np.copy(availMoves)
            dumBoard =np.copy(board)
            dumBoard = gameMove(dumBoard,isMax,availMoves[i],False)
            dumdum = np.delete(dumdum, i)
            score = minimax(dumBoard, not isMax, h, currDepth+1, maxDepth, dumdum)
            if isMax:
                hiScore = max(hiScore,score)
            else:
                loScore = min(loScore,score)
        if isMax:
            return hiScore
        else:
            return loScore
        
       


        
    
            
sys.setrecursionlimit(10**6)
gameBoard = createGameBoard()
pvp = input("Would you like to play agains the computer (y/n)? ")
player = "X"
if pvp=="y":
    pvp = False
    player = input("Would you like to play as X or O? ")
else:
    pvp = True
player2 = True
if player == "X":
    player = False
else:
    player = True
    player2 = False
isPlayerOsMove=True

if pvp: 
    while isGameWon(gameBoard):
        printGameBoard(gameBoard)
        if(isPlayerOsMove):
            move = input("O's move (1-9): ")
            move = int(move)
            gameBoard=gameMove(gameBoard,True,move,False)
            isPlayerOsMove = not isPlayerOsMove
        else:
            move = input("X's move (1-9): ")
            move = int(move)
            gameBoard=gameMove(gameBoard,False,move,False)
            isPlayerOsMove = not isPlayerOsMove
    printGameBoard(gameBoard)
else:
    while isGameWon(gameBoard):
        printGameBoard(gameBoard)
        if player:
            move = input("O's move (1-9): ")
            move = int(move)
            gameBoard=gameMove(gameBoard,True,move,False)
            player = not player
        else:
            gameBoard = gameMove(gameBoard, False, bestMove(gameBoard, player2, 5), False)
            player = not player
    printGameBoard(gameBoard)


            
