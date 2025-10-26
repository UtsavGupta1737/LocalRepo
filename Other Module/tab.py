import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 700), 0, 32)

img = pygame.image.load('a.png')
img_rect = img.get_rect(center = (10,10))

class OBJECT():
	def __init__(self,pos):
		self.pos = pos
		self.clicked = False
		self.img = pygame.image.load('a.png')
		self.rect = img.get_rect(center = self.pos)

	def dis(self,screen):
		screen.blit(self.img,self.rect)

    def move(self):
        print(self.pos.x)



a = OBJECT((10,10))
data = [a]

while True:
        screen.fill('Black')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                data.append(OBJECT(event.pos))

                
        for obj in data:
            obj.gravity()
            obj.dis(screen)
       	
       

        pygame.display.update()
        fpsClock.tick(FPS)

