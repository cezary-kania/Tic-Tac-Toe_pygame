import sys, pygame, time
from pygame.locals import *
from GameBoard import GameBoard
from GameModel import GameModel

class GameController:
    def __init__(self):
        # Init env
        self.screen = pygame.display.set_mode((470,520))
        pygame.display.set_caption('Tic Tac Toe by CezaryK')
        # Init game components 
        self.gameBoard = GameBoard(self.screen)
        self.gameModel = GameModel()
        
    def GameLoop(self):
        while True:
            
            self.screen.fill((0,0,0))
            self.gameBoard.DrawBoard()
            score = self.gameModel.GetScore()
            self.gameBoard.DrawScore(score)
            self.DrawCells()
            self.gameBoard.DrawResetBtn()
            gameState = self.gameModel.IsGameOver()
            for event in pygame.event.get():
                self.HandleUserEvent(event,gameState)
            pygame.display.flip()
    
    def MakeMove(self, cellNum):
        self.gameModel.PlayerMove(cellNum)
    
    def DrawCells(self):
        for i in range(len(self.gameModel.board)):
            mark = self.gameModel.board[i]
            if mark == 'X':
                self.gameBoard.DrawCross(i)
            elif mark == 'O':
                self.gameBoard.DrawCircle(i)
    
    def HandleUserEvent(self,event, gameState):
        if event.type == QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if self.gameBoard.resetBtn.collidepoint(x,y):
                self.gameModel.ResetGame(gameState[1])
                return
            if gameState[0] == False:
                for i in range(9):
                    if self.gameBoard.boardCells[i].collidepoint(x,y):
                        self.MakeMove(i) 
                        return

                