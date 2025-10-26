import pygame,sys,math,time
from grid import Grid
from pygame.locals import *
from pygame.math import Vector2 as vector

pygame.init()


clock = pygame.time.Clock()
fps = 60
size = (1000,700)
screen = pygame.display.set_mode(size)

#----------------- INITIALIZATION --------------------
grid = Grid(screen)


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

	dt = clock.tick() / 1000

	screen.fill('black')

	grid.run(dt, event)
	draw()
	

	# print(clock.get_fps())
	clock.tick(fps)
	pygame.display.update()


