import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, gapStart, SCREENWIDTH):
        super().__init__(self)
        self.pipeStartX = SCREENWIDTH
        self.gapStart = gapStart

    def drawPipe(self, pipeStartX, pipeStartY, pipeWidth, pipeHeight, PIPECOLOR):
        pygame.draw.rect(gameDisplay, PIPECOLOR, [pipeStartX, pipeStartY, pipeWidth, pipeHeight])
        pygame.draw.rect(gameDisplay, PIPECOLOR, [pipeStartX, pipeStartY + pipeHeight + GAPSIZE, pipeWidth, SCREENHEIGHT - pipeHeight - GAPSIZE])
