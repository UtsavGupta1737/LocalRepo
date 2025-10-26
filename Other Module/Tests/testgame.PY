import pygame,sys
from pygame.locals import *
from settings import *

pygame.init()

class Testgame():
	def __init__(self):
		self.clock = pygame.time.Clock()
		self.screen = None
		self.index = 1

	# ---------D R A W-----------
	def draw_screen(self,):
		self.screen.fill('Black')

	# ---------E V E N T-----------
	def event_handling(self):
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit() 
				if pygame.key.get_pressed()[pygame.K_DOWN]:
					self.index = 0

	# ---------U P D A T E-----------
	def update(self):
		pygame.display.update()
		self.clock.tick(FPS)

	# ---------O T H E R S-----------


	# ---------- MAIN GAME LOOP -----------
	def run(self,screen):
		self.index = 1
		self.screen = screen
		while self.index == 1:
			
			# EVENT HANDLING
			self.event_handling()

			# UPDATE
			self.update()

			# DRAW
			self.draw_screen()

		

