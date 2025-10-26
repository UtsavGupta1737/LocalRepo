import pygame,sys,math,time
from settings import *
from star import *
from pygame.locals import *


pygame.init()


clock = pygame.time.Clock()
fps = 60
size = (width,height)
screen = pygame.display.set_mode(size)

#----------------- INITIALIZATION --------------------



stars = []
for i in range(1000):
	star = Star()
	stars.append(star)

#-----------------------------------------------------


#================= FUNCTIONS =========================
def setup():
	pass

def draw():
	for star in stars:
		star.update()
		star.show(screen)




#=====================================================

setup()


while(True):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()




	dt = clock.tick() / 1000

	screen.fill('black')

	draw()
	

	print(clock.get_fps())
	clock.tick(fps)
	pygame.display.update()



