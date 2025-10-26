import pygame,sys,random
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
fps = 60

colors = []
for i in range(250000):
	colors.append(random.randint(0,1))

#===================== FUNCTIONS =====================
def draw(screen):
	for i in range(500):
		for j in range(500):
			color = (0,0,0)
			if colors[i+j] == 1:
				color = (255,255,255)
			pygame.gfxdraw.pixel(screen, i, j, color)

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
	

	print(clock.get_fps())
	clock.tick(fps)
	pygame.display.update()



