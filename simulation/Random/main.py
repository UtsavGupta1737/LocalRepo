import pygame,sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((100,100))
clock = pygame.time.Clock()
fps = 60


#===================== FUNCTIONS =====================
def draw(screen):
	pass

def setup():
	pass

#=====================================================

setup()

#-------------------------- MAIN ---------------------
while(True):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()




	dt = clock.tick() / 1000

	screen.fill('black')

	draw(screen)
	

	# print(clock.get_fps())
	clock.tick(fps)
	pygame.display.update()






