import pygame 
from pygame.locals import *
from settings import *
from grid import *
from testgame import *

pygame.init()

class Menu():
	def __init__(self,main):
		pass



	# ---------D R A W-----------
	def draw_screen(self):
		pygame.draw.rect(main.screen, 'Red', (100,100)) 
		
	

	# ---------E V E N T-----------
	def event_handling(self):
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit() 
			

	# ---------U P D A T E-----------
	def update(self):
		pass
	

	# ---------O T H E R S-----------

			

	# ---------- MAIN GAME LOOP -----------
	def run(self):

		# EVENT HANDLING
		self.event_handling()

		# UPDATE
		self.update()

		# DRAW
		self.draw_screen()


		
		