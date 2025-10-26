import pygame,sys,math,time
from pygame.locals import *

pygame.init()


clock = pygame.time.Clock()
fps = 60
size = (1000,700)
screen = pygame.display.set_mode(size)

#----------------- INITIALIZATION --------------------



#-----------------------------------------------------


#================= FUNCTIONS =========================
def setup():
	pass

def draw():
	pass



#=====================================================

setup()


while(True):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

	screen.fill('black')

	draw()
	

	# print(clock.get_fps())
	clock.tick(fps)
	pygame.display.update()

