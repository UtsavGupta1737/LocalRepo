import pygame,sys,time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

test_rect = pygame.Rect(0,175,50,50)
test_rect_pos = test_rect.x
speed = 100

previous_time = time.time()    # current time
while True:
	dt = time.time() - previous_time
	previous_time = time.time()
	# dt = clock.tick(60) / 1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('White')
	test_rect_pos += speed * dt
	test_rect.x = round(test_rect_pos)
	pygame.draw.rect(screen,'Red',test_rect)

	pygame.display.update()
	