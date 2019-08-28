import pygame
GRAVITY = 0.5

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # initialize the parent sprite class
        super().__init__()

        # Loads the image of the bird
        self.image = pygame.image.load("assets/bird2.png").convert_alpha()
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # The "physics" of the bird
        self.counter = 0
        self.speed = 0

        # the starting position of the bird
        self.rect.x = 150
        self.rect.y = 275

        # will be used for the fitness of the NN
        self.score = 0

    def jump(self):
        # how much the bird will move when told to jump
        self.speed = 8
        self.counter = 4

    def move(self):
        # Calculates the poistion of the bird
        if self.counter is 0:
            self.rect.y += self.speed
            self.speed += GRAVITY
        else:
            self.rect.y -= self.speed
            self.speed -= GRAVITY
            self.counter -= 1
            if self.counter is 0:
                self.speed = 0
