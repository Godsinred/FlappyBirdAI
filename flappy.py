import pygame
import time
import random
from pipe import Pipe
from bird import Bird

# constants
SCREENWIDTH = 900
SCREENHEIGHT = 600

GAPSIZE = 200

BLACK = (0,0,0)
WHITE = (255,255,255)

PIPECOLOR = (0,128,0)
BIRDHEIGHT = 50
PIPEWIDTH = 100
PIPESPEED = 10

def pipesDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+ str(count), True, BLACK)
    gameDisplay.blit(text,(0,0))

class Game():
    def __init__(self):
        pass

def main():
    # initializes the pygame
    pygame.init()
    gameDisplay = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()

    # Drawing on Screen
    gameDisplay.fill(WHITE)

    # creates the birds
    bird = Bird(200, 400)

    # creates all the pipes
    pipe1 = Pipe(0, 0, PIPEWIDTH, 200)
    pipe2 = Pipe(0, 0, PIPEWIDTH, 200)
    pipe3 = Pipe(0, 0, PIPEWIDTH, 100)
    pipe4 = Pipe(0, 0, PIPEWIDTH, 300)
    pipe5 = Pipe(0, 0, PIPEWIDTH, 300)
    pipe6 = Pipe(0, 0, PIPEWIDTH, 100)
    pipe1.rect.x = SCREENWIDTH
    pipe2.rect.x = SCREENWIDTH
    pipe2.rect.y = SCREENHEIGHT - 200
    pipe3.rect.x = SCREENWIDTH * 1.5
    pipe4.rect.x = SCREENWIDTH * 1.5
    pipe4.rect.y = SCREENHEIGHT - 300
    pipe5.rect.x = SCREENWIDTH * 2
    pipe6.rect.x = SCREENWIDTH * 2
    pipe6.rect.y = SCREENHEIGHT - 100

    # Container for all the sprites
    allSpritesList = pygame.sprite.Group()
    allSpritesList.add(bird)
    allSpritesList.add(pipe1)
    allSpritesList.add(pipe2)
    allSpritesList.add(pipe3)
    allSpritesList.add(pipe4)
    allSpritesList.add(pipe5)
    allSpritesList.add(pipe6)

    # container for all the birds
    allBirdList = pygame.sprite.Group()
    allBirdList.add(bird)

    # container for all the pipes
    allPipesList = pygame.sprite.Group()
    allPipesList.add(pipe1)
    allPipesList.add(pipe2)
    allPipesList.add(pipe3)
    allPipesList.add(pipe4)
    allPipesList.add(pipe5)
    allPipesList.add(pipe6)



    # Vars for determining if the game is over
    gameOver = False
    clock = pygame.time.Clock()

    while not gameOver:
            # eventually this needs to be until all the birds are dead
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True

            # this will eventuyally be depricated and replaced by per bird
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                bird.jump()
            if keys[pygame.K_DOWN]:
                bird.fall()

            # Will move all the birds
            for bird in allBirdList:
                bird.move()
                if (bird.rect.y > SCREENHEIGHT or bird.rect.y < 0):
                    print("Out of screen.")
                    gameOver = True

            # Moves the pipes
            for pipe in allPipesList:
                pipe.moveLeft()
                if pipe.rect.x + PIPEWIDTH < 0:
                    pipe.reset()

            # Collision detection area
            pipeCollision = pygame.sprite.groupcollide(allPipesList, allBirdList, False, False)
            for bird in pipeCollision:
                print("bird collision")
                #End Of Game
                gameOver = True

            allSpritesList.update()

            #Drawing on Screen
            gameDisplay.fill(WHITE)

            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            allSpritesList.draw(gameDisplay)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    # Exits
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
