import pygame

pygame.init()

class GameBoard:
    boardCells = [pygame.Rect(xCord,yCord,150,150) for yCord in [0,160,320] for xCord in [0,160,320]]
    boardCellsCords = [cell.center for cell in boardCells]
    resetBtn = None
    def __init__(self, screen):
        self.screen = screen

    def DrawBoard(self):
        for cell in self.boardCells:
            pygame.draw.rect(self.screen,(255,255,255),cell)
    
    def CreateCross(self):
        s1 = pygame.Surface((120,10))
        s2 = pygame.Surface((120,10))
        s1.set_colorkey((255,255,255))
        s2.set_colorkey((255,255,255))
        s1.fill((0,0,255))
        s2.fill((0,0,255))
        s1 = pygame.transform.rotate(s1, 45)
        s2 = pygame.transform.rotate(s2, -45)
        
        rec1 = s1.get_rect()
        rec2 = s2.get_rect()
        rec1.center = (75,75)
        rec2.center = (75,75)

        cross = pygame.Surface((150,150))
        cross.fill((255,255,255))
        cross.blit(s1,rec1)
        cross.blit(s2,rec2)

        return cross

    def DrawCross(self,cellNum):
        xCord, yCord = self.boardCellsCords[cellNum]
        myCross = self.CreateCross()
        myCross_rec = myCross.get_rect()
        myCross_rec.center = (xCord, yCord)
        self.screen.blit(myCross,myCross_rec)

    def DrawCircle(self,cellNum):
        xCord, yCord = self.boardCellsCords[cellNum]
        pygame.draw.circle(self.screen, (255,0,0),(xCord, yCord), 55,10)
        
    def DrawScore(self,score):
        font = pygame.font.SysFont('comicsansms',16)
        
        p1TextSurface = font.render(f'Player 1: {score["X"]}',True,(255,255,255))
        p1TextRect = p1TextSurface.get_rect()
        p1TextRect.center = (75,495)
        self.screen.blit(p1TextSurface,p1TextRect)

        p2TextSurface = font.render(f'Player 2: {score["O"]}',True,(255,255,255))
        p2TextRect = p2TextSurface.get_rect()
        p2TextRect.center = (395,495)
        self.screen.blit(p2TextSurface,p2TextRect)

    def DrawResetBtn(self):
        font = pygame.font.SysFont('comicsansms',16)
        resetBtnSurface = font.render(f'Reset game',True,(255,0,0))
        self.resetBtn = resetBtnSurface.get_rect()
        self.resetBtn.center = (235,495)
        self.screen.blit(resetBtnSurface,self.resetBtn)