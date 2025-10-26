import pygame ,sys
from pygame.locals import *
from random import randint

class OBJECT():
	def __init__(self):
		self.name = 'name'
		self.size = (50,50)
		self.color = 'Red'
		self.pos = (50,50)

	def dis(self,screen):
		self.rect = pygame.Rect((self.size),(self.pos))
		pygame.draw.rect(screen,self.color,self.rect)

class COLL(OBJECT):
	def __init__(slef):
		slef.v = pygame.




pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,400))
ob1 = OBJECT()


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('Black')
	ob1.dis(screen)


	
	

	pygame.display.update()
	clock.tick(60)
