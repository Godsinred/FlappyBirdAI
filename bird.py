import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # initialize the parent sprite class
        super().__init__()

        # initialize the bird attributes
        self.birdX = x
        self.birdY = y
        self.color = (255, 0, 255)

        self.yChange = 10
        self.counter = 0

        self.width=50
        self.height=50

        # # Pass in the color of the car, and its x and y position, width and height.
        # # Set the background color and set it to be transparent
        # self.image = pygame.Surface([self.birdX, self.birdY])
        # self.image.fill(WHITE)
        # self.image.set_colorkey(WHITE)


        # # Draw the car (a rectangle!)
        # pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("assets/bird.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self):
        self.rect.y += 100

    def drawBird(self):
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
