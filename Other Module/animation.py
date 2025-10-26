import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
Clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 300), 0, 32)

class OBJECT():
    def __init__(self):
        self




while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()
        fpsClock.tick(FPS)








