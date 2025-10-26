import pygame ,sys
from setting import *
from pygame.locals import *

class Colli:
#initialisation
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()

		#rectangles
		self.mo_rect = pygame.Rect(100,100,50,50)
		self.ot_rect = pygame.Rect(200,200,100,50)


#drawing rectangles
	def draw_rect(self):
		if self.colli_check(self.mo_rect,self.ot_rect):
			print('*')
		self.move_rect()
		pygame.draw.rect(self.screen,('Red'),self.mo_rect)
		pygame.draw.rect(self.screen,('Blue'),self.ot_rect)

#moving rectangles
	def move_rect(self):
		self.mo_rect.x += 5
		self.mo_rect.y += 5


#collsion detection
	def colli_check(self,rect_1,rect_2):
		if rect_1.colliderect(rect_2):
			return True
		else:
			return False


#event handling
	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		self.draw_rect()

#main loop
	def run(self):
		while True:
			self.screen.fill('White')
			self.event_loop()
			dt = self.clock.tick() / 1000








			
			pygame.display.update()


if __name__	== '__main__':
	colli = Colli()
	colli.run() 
	
