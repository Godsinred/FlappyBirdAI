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
SKYBLUE = (135,206,235)
WHEAT = (245,222,179)

PIPECOLOR = (0,128,0)
BIRDHEIGHT = 50
PIPEWIDTH = 100

HEIGHTGROUND = 100

class Game():
    def __init__(self, populationSize):
        # initializes the pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        # For writing to the screen, currently score
        self.FONT = pygame.font.SysFont("Sans", 20)

        # Drawing on Screen
        self.screen.fill(WHITE)

        # Container for all the sprites
        self.allSpritesList = pygame.sprite.Group()
        # container for all the birds
        self.allBirdList = pygame.sprite.Group()
        # container for all the pipes
        self.allPipesList = pygame.sprite.Group()

        # list of all birds for analysis after the pygame exits
        self.bird = []

        # This is for the NN calculations for determining how far the next pipe is
        # these are in pairs since having one image surface has collision when you
        # try and pass through
        self.pipes = []

        # creates the birds
        self.createBirds(populationSize)
        # creates all the pipes
        # (x, y, width, height)
        self.createPipes()

        # Vars for determining if the game is over
        self.clock = pygame.time.Clock()
        self.startTime = pygame.time.get_ticks()
        self.rand = random.Random(100)

    def createBirds(self, populationSize):
        # for the designated population size we will create that many birds and
        # add them to the allBirdList and allSpritesList
        for i in range(populationSize):
            bird = Bird(200, 400, i)
            self.allBirdList.add(bird)
            self.allSpritesList.add(bird)
            self.bird.append(bird)

    def createPipes(self):
        # creates all the pipes
        # (x, y, width, height)
        pipe1 = Pipe(0, 0, PIPEWIDTH, 200, 0)
        pipe2 = Pipe(0, 0, PIPEWIDTH, 200, 1)
        pipe3 = Pipe(0, 0, PIPEWIDTH, 100, 2)
        pipe4 = Pipe(0, 0, PIPEWIDTH, 300, 3)
        pipe5 = Pipe(0, 0, PIPEWIDTH, 250, 4)
        pipe6 = Pipe(0, 0, PIPEWIDTH, 50, 5)
        # Also need to calculate for the ground now
        pipe1.rect.x = SCREENWIDTH
        pipe2.rect.x = SCREENWIDTH
        pipe2.rect.y = pipe1.height + GAPSIZE
        pipe3.rect.x = SCREENWIDTH * 1.5
        pipe4.rect.x = SCREENWIDTH * 1.5
        pipe4.rect.y = pipe3.height + GAPSIZE
        pipe5.rect.x = SCREENWIDTH * 2
        pipe6.rect.x = SCREENWIDTH * 2
        pipe6.rect.y = pipe5.height + GAPSIZE

        # pipe1.rect.union_ip(pipe2.rect)
        self.allPipesList.add(pipe1)
        self.allPipesList.add(pipe2)
        self.allPipesList.add(pipe3)
        self.allPipesList.add(pipe4)
        self.allPipesList.add(pipe5)
        self.allPipesList.add(pipe6)

        self.allSpritesList.add(pipe1)
        self.allSpritesList.add(pipe2)
        self.allSpritesList.add(pipe3)
        self.allSpritesList.add(pipe4)
        self.allSpritesList.add(pipe5)
        self.allSpritesList.add(pipe6)

        # these are in pairs since having one image surface has collision when you
        # try and pass through
        self.pipes = [pipe1, pipe2, pipe3, pipe4, pipe5, pipe6]

def main():

    populationSize = 10
    generations = 1

    for i in range(generations):
        messageGeneration = "Gen: " + str(i + 1)
        print(messageGeneration)
        game = Game(populationSize)

        while game.allBirdList:
                # eventually this needs to be until all the birds are dead
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                # this will eventuyally be depricated and replaced by per bird
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    # hard coded for now but this will change with the NN
                    game.bird[0].jump()
                    game.bird[4].jump()

                # Will move all the birds
                for bird in game.allBirdList:
                    bird.move()
                    if (bird.rect.y > SCREENHEIGHT - HEIGHTGROUND or bird.rect.y < 0):
                        print("Out of screen for genome: " + str(bird.genomeNum))
                        bird.removeBird(pygame.time.get_ticks() - game.startTime)

                # Moves the pipes and determines if we need to move it to the end of the screen
                # num is a random number for determine the pipe heights (SEEDED)
                num = game.rand.randrange(100, SCREENHEIGHT - HEIGHTGROUND - GAPSIZE - 100)
                for pipe in game.allPipesList:
                    pipe.moveLeft()
                    if pipe.rect.x + PIPEWIDTH < 0:
                        pipe.reset(num)

                # Collision detection area
                pipeCollision = pygame.sprite.groupcollide(game.allBirdList, game.allPipesList, False, False)
                for bird in pipeCollision:
                    print("bird collision for genome: " + str(bird.genomeNum))
                    bird.removeBird(pygame.time.get_ticks() - game.startTime)

                game.allSpritesList.update()

                #Drawing on Screen
                game.screen.fill(SKYBLUE)

                # Draws all the sprites on the screen
                game.allSpritesList.draw(game.screen)

                # draws the ground
                pygame.draw.rect(game.screen, WHEAT, [0, SCREENHEIGHT - HEIGHTGROUND, SCREENWIDTH, HEIGHTGROUND])

                curTime = pygame.time.get_ticks()
                messageScore = "Score: " + str(curTime - game.startTime)
                game.screen.blit(game.FONT.render(messageScore, True, BLACK), (20, 20))
                game.screen.blit(game.FONT.render(messageGeneration, True, BLACK), (SCREENWIDTH - 100, 20))

                # Refresh Screen
                pygame.display.flip()

                #Number of frames per secong e.g. 60
                game.clock.tick(60)

        # Exits
        pygame.quit()
        for i in range(populationSize):
            print("Score for genome: " + str(game.bird[i].score))
        del game

        print("sleep 2 <eye break for human>")
        time.sleep(2)

    print("\nEnd of Program.")
    quit()

if __name__ == "__main__":
    main()
