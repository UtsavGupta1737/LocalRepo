import pygame,sys
from pygame.locals import *
from settings import *
from snake import *

screen = pygame.display.set_mode((width,height))
fps = 10 
clock = pygame.time.Clock()



#----------------- INITIALIZATION --------------------
s = Snake()

#-----------------------------------------------------

#================= FUNCTIONS =========================

def setup():
	pass


def draw(screen):
	s.show(screen)
	

#=====================================================

setup()


while(True):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		 
		

		
		
		s.input(event)	

	s.update()


	dt = clock.tick() / 1000

	screen.fill('black')

	draw(screen)
	

	# print(clock.get_fps())
	clock.tick(fps)
	pygame.display.update()

