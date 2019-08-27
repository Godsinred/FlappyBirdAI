import pygame
import time
import random
from pipe import Pipe
from bird import Bird

# constants
SCREENWIDTH = 800
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

    generations = 1
    populationSize = 1

    # for i in range(generations):
    #     curGame = Game(populationSize)
    #     curGame.start()

    pygame.init()
    gameDisplay = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption("Car Racing")
    clock = pygame.time.Clock()

    #Drawing on Screen
    gameDisplay.fill((20, 255, 140))
    all_sprites_list = pygame.sprite.Group()
    bird = Bird(200, 400)
    all_sprites_list.add(bird)

    bird.drawBird()
    time.sleep(5)
    bird.moveUp()
    bird.drawBird()


    time.sleep(5)
    pygame.quit()




    quit()

if __name__ == "__main__":
    main()
