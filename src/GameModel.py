from random import choice
class GameModel:

    def __init__(self):
        self.nextTurn = choice(['X','O'])
        self.board = [None]*9
        self.score = {'X': 0, 'O': 0}

    def ChangePlayer(self):
        if self.nextTurn == 'X':
            self.nextTurn = 'O'
        else:
            self.nextTurn = 'X'
    
    def IsGameOver(self):
        winOptions = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[6,4,2],[0,3,6],[1,4,7],[2,5,8]]
        for option in winOptions:
            if self.board[option[0]] == self.board[option[1]] == self.board[option[2]] and self.board[option[0]] != None:
                winner = self.board[option[0]]
                return True, winner
        if None not in self.board:
            return True, None
        return False, None
    
    def PlayerMove(self, selectedCell):
        if selectedCell > 8 or selectedCell < 0 or self.board[selectedCell] != None:
            return
        self.board[selectedCell] = self.nextTurn
        self.ChangePlayer()

    def ResetGame(self, winner = None):
        if winner is not None:
            self.score[winner] += 1
        if self.board.count(None) == 9:
            self.ScoreReset()
        self.board = [None]*9

    def GetScore(self):
        return self.score
    
    def ScoreReset(self):
        self.score = {'X': 0, 'O': 0}

