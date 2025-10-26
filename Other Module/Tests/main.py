import pygame,sys
from pygame.locals import *
from settings import *
from grid import Grid
from menu import Menu
from testgame import *


class Main:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		self.index = 0
		self.menu = Menu(self)
		self.testgame = Testgame()
		

	# ---------D R A W-----------
	def draw_screen(self):
		menu.run()
		self.screen.fill('Black')
		

	# ---------E V E N T-----------
	def event_handling(self):
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit() 
				if pygame.key.get_pressed()[pygame.K_UP]:
					self.index = 0
					

	# ---------U P D A T E-----------
	def update(self):
		self.selection_index()
		pygame.display.update()
		self.clock.tick(FPS)

	# ---------O T H E R -----------
	def selection_index(self):
		if self.index == 0:
			self.index = self.menu.run(self.screen)
		if self.index == 1:
			self.testgame.run(self.screen)
			self.index = 0


	def run(self):
		while True:

			# EVENT HANDLING
			self.event_handling()

			# UPDATE
			self.update()

			# DRAW
			self.draw_screen()
					


if __name__ == '__main__':
	main = Main()
	main.run() 
