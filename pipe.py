import pygame

WHITE = (255,255,255)
SCREENWIDTH = 900

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        # initialize the parent sprite class
        super().__init__()

        # initializes the pipe attributes
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE) # used for blitting to speed up rendering

        # Pipe attributes
        self.width = width
        self.height = height
        self.color = (0,128,0)

        # Draws the rectangle to the screen with in the surface coordinates
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Fetch the rectangleobject that has the dimensions of the image
        self.rect = self.image.get_rect()

    # moves the pipe left a fixed number of pixels
    def moveLeft(self):
        self.rect.x -= 3

    # resets the pipe attributes to be drawn again later
    def reset(self):
        self.rect.x = SCREENWIDTH * 1.5
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
