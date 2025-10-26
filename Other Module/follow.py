import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
WHITE = (255, 255, 255)
img = pygame.image.load('a.png')
img_rect = img.get_rect(center = (10,10))
clicked = False


while True:
     # the main game loop
        DISPLAYSURF.fill('Black')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print()
                if event.type == pygame.MOUSEMOTION:
                    img_rect.center = event.pos
        DISPLAYSURF.blit(img,img_rect)
        pygame.draw.rect(DISPLAYSURF,'White',img_rect)

        pygame.display.update()
        fpsClock.tick(FPS)









