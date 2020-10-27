import tkinter
from tkinter import *
import numpy as np
import time

class TikTakToe:
    def __init__(self):
        self.gameBoard = self.createGameBoard()
        self.gameBoardString = self.convertBoardToString(self.gameBoard)
        self.playerIsX = False
        self.pvp = False
        self.isPlayerOsMove = True
        self.buttonHasNotBeenPressed = True
        self.root = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.root)
        self.button1=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(0,0, self.button1))
        self.button2=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(0,1, self.button2))
        self.button3=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(0,2, self.button3))
        self.button4=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(1,0, self.button4))
        self.button5=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(1,1, self.button5))
        self.button6=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(1,2, self.button6))
        self.button7=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(2,0, self.button7))
        self.button8=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(2,1, self.button8))
        self.button9=tkinter.Button(self.top_frame, text=" ", command = lambda : self.buttonPress(2,2, self.button9))
        self.buttonList = [self.button1, self.button2, self.button3, self.button4, self.button5, 
         self.button6, self.button7, self.button8, self.button9]

    def startGame(self, v1, v2):

        for button in self.buttonList:
            button['text'] = ' '

        self.gameBoard = self.createGameBoard()

        self.isPlayerOsMove = True

        if(v1 == '1'):
            self.playerIsX = True
        else:
            self.playerIsX = False
        if(v2 == '1'):
            self.pvp = False
        else:
            self.pvp = True
        if(not self.pvp):
            self.runGameAI()

    def runGameAI(self):
        return 0


    def isGameWon(self):
        if self.gameBoard[0,0] == self.gameBoard[0,1] == self.gameBoard[0,2]:
            return True
        if self.gameBoard[1,0] == self.gameBoard[1,1] == self.gameBoard[1,2]:
            return True
        if self.gameBoard[2,0] == self.gameBoard[2,1] == self.gameBoard[2,2]:
            return True
        if self.gameBoard[0,0] == self.gameBoard[1,0] == self.gameBoard[2,0]:
            return True
        if self.gameBoard[0,1] == self.gameBoard[1,1] == self.gameBoard[2,1]:
            return True
        if self.gameBoard[0,2] == self.gameBoard[1,2] == self.gameBoard[2,2]:
            return True
        if self.gameBoard[0,0] == self.gameBoard[1,1] == self.gameBoard[2,2]:
            return True
        if self.gameBoard[0,2] == self.gameBoard[1,1] == self.gameBoard[2,0]:
            return True
        return False

    def convertBoardToString(self, board):
        string = ""
        #for i in range(11):
        #   for j in range(11):
        #      string  +=  ''+str(board[j,i])
        # string += '\n'
        return string


    def createGameBoard(self):
        gameboard = np.empty([3,3],dtype=int)
        counter = 1
        for i in range(3):
            for j in range(3):
                gameboard[i,j]=counter
                counter = counter+1
        return gameboard

    def buttonPress(self, row, column, button):
        if not self.isGameWon() and self.gameBoard[row,column]>0: 
            if self.isPlayerOsMove:
                button["text"] = "O"
                self.gameBoard[row,column] = -1
            else:
                button["text"] = "X"
                self.gameBoard[row,column] = -2
            if self.isGameWon():
                print("gamewon")
            self.isPlayerOsMove = not self.isPlayerOsMove
            self.buttonHasNotBeenPressed = False
        else:
            return

    def tikTakToeGuiLaunch(self):
        #Create a root window
        mid_frame = tkinter.Frame(self.root)
        mid2_frame = tkinter.Frame(self.root)
        bottom_frame = tkinter.Frame(self.root)
        pvpButton = tkinter.Label(mid2_frame, text = "Opponent?")
        playerSelection = tkinter.Label(mid2_frame, text = "Which player?")
    
        # Tkinter string variable 
        # able to store any string value 
        v1 = StringVar(self.root, "1") 

        self.button1.grid(row=0,column=0)
        self.button2.grid(row=0,column=1)
        self.button3.grid(row=0,column=2)
        self.button4.grid(row=1,column=0)
        self.button5.grid(row=1,column=1)
        self.button6.grid(row=1,column=2)
        self.button7.grid(row=2,column=0)
        self.button8.grid(row=2,column=1)
        self.button9.grid(row=2,column=2)
    
    

  
        # Dictionary to create multiple buttons 
        values = {"Player 'X'" : "1", 
              "Player 'O'" : "2", } 
  
        # Loop is used to create multiple Radiobuttons 
        # rather than creating each button separately 
        for (text, value) in values.items(): 
            Radiobutton(bottom_frame, text = text, variable = v1,  
                    value = value,  
                    background = "light blue").pack( side = 'left', ipady = 5)

        v2 = StringVar(self.root, "2") 
  
        # Dictionary to create multiple buttons 
        values = {"PVAI" : "1", 
              "PVP" : "2", } 
  
        # Loop is used to create multiple Radiobuttons 
        # rather than creating each button separately 
        for (text, value) in values.items(): 
            Radiobutton(bottom_frame, text = text, variable = v2,  
                    value = value,  
                    background = "light blue").pack(side = 'right', ipady = 5) 
   
        playButton = tkinter.Button(mid_frame, text = 'PLAY', command = lambda : self.startGame(v1.get(),
         v2.get()))
        playButton.pack()
        pvpButton.pack(side = 'right')
        playerSelection.pack(side = 'left')
        #Call the event loop
        self.top_frame.pack(side = 'top')
        bottom_frame.pack(side = 'bottom')
        mid2_frame.pack(side = 'bottom')
        mid_frame.pack(side = 'top')
        self.root.mainloop()




def main():
    game = TikTakToe()
    game.tikTakToeGuiLaunch()
    
#Call the function main
main()