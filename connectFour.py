import numpy as np
import sys

def createGameBoard():
    gameBoard = np.empty([6,7],dtype=object)
    for row in range(6):
        for col in range(7):
            gameBoard[row,col] = 0
    return gameBoard

def printGameBoard(gameBoard):
    for row in range(5,-1,-1):
        for col in range(7):
            print(gameBoard[row,col],end=' ')
        print('\n')

def isGameWon(gameBoard):
    tracker = np.zeros([3])
    lastValue = 'n'
    for row in range(6):
        for col in range(7):
            if lastValue == gameBoard[row,col] and gameBoard[row,col] != 0:
                tracker[0] = tracker[0]+1
            else:
                lastValue = gameBoard[row,col]
                tracker[0] = 0
            if tracker[0] == 3 and gameBoard[row,col] != 0:
                return True, gameBoard[row,col]
    lastValue = 'n'
    for i in range(7):
        for j in range(6):
            if lastValue == gameBoard[j,i] and gameBoard[j,i] != 0:
                tracker[1] = tracker[1]+1
            else:
                lastValue = gameBoard[j,i]
                tracker[1] = 0
            if tracker[1] == 3 and gameBoard[j,i] != 0:
                return True, gameBoard[j,i]
    for row in range(3):
        for col in range(4):
            if gameBoard[row,col]==gameBoard[row+1,col+1] and gameBoard[row,col] != 0:
                if gameBoard[row+2,col+2] == gameBoard[row+1,col+1]:
                    if gameBoard[row+3,col+3]==gameBoard[row,col]:
                        return True, gameBoard[row,col]
            elif gameBoard[row,col+3]==gameBoard[row+1,col+2] and gameBoard[row,col+3] != 0:
                if gameBoard[row+2,col+1] == gameBoard[row+1,col+2]:
                    if gameBoard[row+3,col]==gameBoard[row,col+3]:
                        return True, gameBoard[row,col+3]
    dum = 0
    for col in range(7):
        if gameBoard[5,col] != 0:
            dum = dum+1
    if dum == 7:
        return True, -1
    return False, 0

def gameMove(gameBoard,move,isY):
    for i in range(6):
        if isMoveValid(gameBoard,move):
            if gameBoard[i,move] == 0:
                if isY:
                    gameBoard[i,move] = 1
                else:
                    gameBoard[i,move] = 2
                return gameBoard
        else:
            move = input("enter new move (0-6): ")
            move = int(move)
            return gameMove(gameBoard,move,isY)
        
            


def isMoveValid(gameBoard, move):
    tracker = True
    #sprint(move)
    if gameBoard[5,move] == 0:
        pass
    else:
        tracker = False
    return tracker

def bestMove(board, isMax, maxDepth):
    score = 0
    hiScore = -1000000
    loScore = 1000000
    move = 0
    dumBoard = 0
    availMoves = np.array([])
    for i in range(7):
        if isMoveValid(board,i):
            availMoves = np.append(availMoves, i)
    print(availMoves)
    dumMoves = np.copy(availMoves)
    for i in range(len(availMoves)):
        dumBoard = np.copy(board)
        dumMoves = np.copy(availMoves)
        print(availMoves[i])
        if not isMoveValid(dumBoard, i):
            dumMoves = np.delete(dumMoves, i)
        dumBoard = gameMove(dumBoard, int(availMoves[i]), isMax)
        score = minimax(dumBoard, not isMax, 0, dumMoves, maxDepth)
        print(score)
        if isMax:
            if score >= hiScore:
                hiScore = score
                move = availMoves[i]
        else:
            if score <= loScore:
                loScore = score
                move = availMoves[i]
    return int(move)

def minimax(gameBoard, isMax, currDepth, availMoves, maxDepth):
    dumdum=np.copy(availMoves)
    dumBoard = 0
    hiScore = -1000000
    loScore = 10000000
    score = 0
    
    #print(isGameWon(gameBoard)[1])
    if isGameWon(gameBoard)[1]==2:
        return -100+currDepth
    elif isGameWon(gameBoard)[1]==1:
        return 100-currDepth
    elif isGameWon(gameBoard)[1]==-1:
        return 0
    if currDepth == maxDepth:
        return heuristic(gameBoard)
    else:
        for i in range(len(availMoves)):
            dumdum = np.copy(availMoves)
            dumBoard =np.copy(gameBoard)
            if not isMoveValid(dumBoard, i):
                dumBoard = gameMove(dumBoard,int(availMoves[i]),isMax)
            
                dumdum = np.delete(dumdum, i)
            score = minimax(dumBoard, not isMax,currDepth+1, dumdum, maxDepth)
            if isMax:
                hiScore = max(hiScore,score)
            else:
                loScore = min(loScore,score)
        if isMax:
            return hiScore
        else:
            return loScore

def heuristic(gameBoard):
    score = 0
    for i in range(6):
        if gameBoard[i,3] ==2:
            score = score - 1
        if gameBoard[i,3] == 1:
            score = score + 1
    tracker = np.zeros([3])
    lastValue = 'n'
    for row in range(6):
        for col in range(3):
            tracker = np.zeros([3])

            if gameBoard[row,col]==0:
                tracker[0] = tracker[0]+1
            elif gameBoard[row,col]==1:
                tracker[1] = tracker[1]+1
            else:
                tracker[2] = tracker[2]+1

            if gameBoard[row, col+1]==0:
                tracker[0] = tracker[0]+1
            elif gameBoard[row,col+1]==1:
                tracker[1] = tracker[1]+1
            else:
                tracker[2] = tracker[2]+1

            if gameBoard[row, col+2] == 0:
                tracker[0] = tracker[0]+1
            elif gameBoard[row,col+2]==1:
                tracker[1] = tracker[1]+1
            else:
                tracker[2] = tracker[2]+1

            if gameBoard[row, col+3] == 0:
                tracker[0] = tracker[0]+1
            elif gameBoard[row,col+3]==1:
                tracker[1] = tracker[1]+1
            else:
                tracker[2] = tracker[2]+1
            
            if tracker[0] == 3 and tracker[1]==1:
                score = score + 1
            elif tracker[2]==1 and tracker[0] == 3:
                score = score - 1
            if tracker[0] == 2 and tracker[1]==2:
                score = score + 5
            elif tracker[0] == 2 and tracker[2]==2:
                score = score -5
            if tracker[0] == 1 and tracker[1] == 3:
                score = score + 20
            elif tracker[0] == 1 and tracker [2] == 3:
                score = score -20
            
    lastValue = 'n'
    for i in range(7):
        for j in range(6):
            if lastValue == gameBoard[j,i] and gameBoard[j,i] != 0:
                tracker[1] = tracker[1]+1
            else:
                lastValue = gameBoard[j,i]
                tracker[1] = 0
            if tracker[1] == 2 and gameBoard[row,col]==2:
                score = score - 5
            elif tracker[1] ==2 and gameBoard[row,col] == 1:
                score = score + 5
            if tracker[0] == 1 and gameBoard[row,col]==2:
                score = score - 1
            elif tracker[0] ==1 and gameBoard[row,col] == 1:
                score = score + 1
    return score

sys.setrecursionlimit(10**6)
gameBoard = createGameBoard()
h = input("would you like to play against the computer? (y/n): ")
isY = True
if h == 'n':
    while not isGameWon(gameBoard)[0]:
        printGameBoard(gameBoard)
        move = int(input("enter a move (0-6): "))
        gameBoard = gameMove(gameBoard, move,isY)
        isY = not isY
    printGameBoard(gameBoard)
else:
    player = int(input("would you like to play as 1 or 2: "))
    if player == 1:
        isMax = False
    else:
        isMax = True
        isY = False
    while not isGameWon(gameBoard)[0]:
        printGameBoard(gameBoard)
        if isY:
            move = int(input("enter a move (0-6): "))
            gameBoard = gameMove(gameBoard, move,isY)
            isY = not isY
        else:
            gameBoard = gameMove(gameBoard, bestMove(gameBoard,isMax,2), isY)
            isY = not isY

