import pygame
import time
import random

pygame.init()

screenWidth = 800
screenHeight = 600

BLACK = (0,0,0)
WHITE = (255,255,255)

blockColor = (0,128,0)

birdHeight = 50

gameDisplay = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

birdImg = pygame.image.load("assets/bird.png")

def pipesDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, BLACK)
    gameDisplay.blit(text,(0,0))

def drawPipe(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def drawBird(x,y):
    gameDisplay.blit(birdImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screenWidth/2),(screenHeight/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game()



def crash():
    message_display("Game Over")

def game():
    birdX = (screenWidth * 0.2)
    birdY = (screenHeight * 0.5)

    yChange = 10
    counter = 0

    pipeStartX = screenWidth
    pipeStartY = 0
    pipeSpeed = 10
    pipeWidth = 100
    pipeHeight = 200

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


        drawPipe(pipeStartX, pipeStartY, pipeWidth, pipeHeight, blockColor)


        pipeStartX -= pipeSpeed
        drawBird(birdX,birdY)
        pipesDodged(score)

        if birdY > screenHeight - birdHeight or birdY < 0:
            crash()

        if pipeStartX + pipeWidth < birdX:
            pipeStartY = 0
            pipeStartX = screenWidth
            pipeHeight = 400 * random.random()
            score += 1

        if birdY < pipeStartY + pipeHeight:
            print('birdY crossover')

            if birdX > pipeStartX and birdX < pipeStartX + pipeWidth:
                print('birdX crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game()
pygame.quit()
quit()
