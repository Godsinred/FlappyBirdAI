import pygame
import random

WHITE = (255,255,255)
SCREENWIDTH = 900
SCREENHEIGHT = 600
GAPSIZE = 200
HEIGHTGROUND = 100

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, num):
        # initialize the parent sprite class
        super().__init__()

        # unique identifier
        self.pipeNum = num
        # initializes the pipe attributes
        self.image = pygame.Surface([width, height])
        self.image.fill((0,128,0))
        self.image.set_colorkey(WHITE) # used for blitting to speed up rendering

        # Pipe attributes
        self.width = width
        self.height = height
        self.color = (0,128,0)

        # Draws the rectangle to the screen with in the surface coordinates
        # pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Fetch the rectangleobject that has the dimensions of the image
        self.rect = self.image.get_rect()

    # moves the pipe left a fixed number of pixels
    def moveLeft(self):
        # self.rect.x -= 5
        self.rect.move_ip(-5,0)

    # resets the pipe attributes to be drawn again later
    def reset(self, height):
        if self.pipeNum % 2 is not 0:
            height = SCREENHEIGHT - GAPSIZE - height

        # need to recreate image for the collisionn detecction
        self.image = pygame.Surface([self.width, height])
        self.image.fill((0,128,0))
        self.image.set_colorkey(WHITE) # used for blitting to speed up rendering

        self.rect = self.image.get_rect()
        self.rect.x = SCREENWIDTH * 1.5

        if self.pipeNum % 2 is not 0:
            self.rect.y = SCREENHEIGHT - height 
