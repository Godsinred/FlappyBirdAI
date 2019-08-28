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
    text = font.render("Score: "+str(count), True, BLACK)
    gameDisplay.blit(text,(0,0))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREENWIDTH/2),(SCREENHEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game()



def crash():
    message_display("Game Over")

### IGNORE THIS FOR NOW, was going to put the game into a class how we discussed
class Game():
    def __init__(self):
        pygame.init()

        self.gameDisplay = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

        self.birdImg = pygame.image.load("assets/bird.png")
        pygame.quit()

        # seeded random so that the game always gets the same set of pipes in each generation
        random.seed(1337)

        score = 0

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        yChange = -10
                        counter = 10

                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #         yChange = 5


            if counter > 0:
                counter -= 1
            else:
                yChange = 10

            birdY += yChange

            gameDisplay.fill(WHITE)


            drawPipe(pipeStartX, pipeStartY, pipeWidth, pipeHeight, PIPECOLOR)


            pipeStartX -= pipeSpeed
            drawBird(birdX,birdY)
            # can just draw an extra bird but will have to keep and check for collision
            # drawBird(birdX,birdY + 100)
            pipesDodged(score)

            if birdY > SCREENHEIGHT - BIRDHEIGHT or birdY < 0:
                crash()

            if pipeStartX + pipeWidth < birdX:
                pipeStartY = 0
                pipeStartX = SCREENWIDTH
                pipeHeight = 400 * random.random()
                score += 1

            if (birdY < pipeStartY + pipeHeight) or (birdY > pipeStartY + pipeHeight + GAPSIZE):
                print('birdY crossover')

                if birdX > pipeStartX and birdX < pipeStartX + pipeWidth:
                    print('birdX crossover')
                    crash()

            pygame.display.update()
            clock.tick(60)

    def start(self):
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

            for bird in allBirdList:
                bird.move()

            # Game Logic
            for pipe in allPipesList:
                pipe.moveLeft()
                if pipe.rect.x + PIPEWIDTH < 0:
                    pipe.reset()

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

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
