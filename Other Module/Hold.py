import pygame,sys,math,time
from pygame.locals import *

pygame.init()


clock = pygame.time.Clock()
fps = 60
size = (1000,700)
screen = pygame.display.set_mode(size)

#----------------- INITIALIZATION --------------------

test_box_pos = [100,100]			# Center Pos
test_box_size = [50,50]
lift = False						# Check when lifted






#-----------------------------------------------------


#================= FUNCTIONS =========================
def setup():
	pass

def event_manager():
	if 




def gravity(dt):
	bottom = test_box_pos[1] + test_box_size[1]/2
	print(bottom)
	if (bottom < size[1]):
		test_box_pos[1] += 1000 * dt

	if (bottom > size[1]):									# Clipping to Ground
		test_box_pos[1] = size[1] - test_box_size[1] / 2


def draw(screen,dt):
	offset_pos = [0,0]
	offset = [test_box_size[0]/2,test_box_size[1]/2]

	offset_pos[0] = test_box_pos[0] - offset[0]
	offset_pos[1] = test_box_pos[1] - offset[1]

	pygame.draw.rect(screen,'White',Rect(offset_pos,test_box_size))



#=====================================================

setup()

pre_time = time.time()
while(True):
	dt = time.time() - pre_time
	pre_time = time.time()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if 

	screen.fill('black')

	event_manager()


	gravity(dt)

	draw(screen,dt)
	

	print(clock.get_fps())
	clock.tick(fps)
	pygame.display.update()
