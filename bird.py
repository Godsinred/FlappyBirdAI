import pygame
GRAVITY = 5

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # initialize the parent sprite class
        super().__init__()

        # Loads the image of the bird
        self.image = pygame.image.load("assets/bird.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # The "physics" of the bird
        self.yChange = 10
        self.counter = 0
        self.speed = 0

        self.rect.x = 150
        self.rect.y = 275

    def jump(self):
        self.speed = 20
        self.counter = 5

    def fall(self):
        self.rect.y += 10

    def move(self):
        if counter is 0:
            self.rect.y += self.speed
            self.speed += GRAVITY
        else:
            self.rect.y -= self.speed
