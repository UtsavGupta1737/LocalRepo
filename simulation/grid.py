import pygame, sys 
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos

class Grid:
	# initialisation
	def __init__(self,screen):

		# main setup 
		self.display_surface = screen

		# navigation
		self.origin = vector()
		self.pan_active = False
		self.pan_offset = vector()

		# support surface
		self.support_surf = pygame.display.get_surface()
		self.support_surf.set_colorkey('green')
		self.support_surf.set_alpha(30)

	def event_loop(self, event):
		pass


	# drawing	
	def draw_grid_lines(self):
   		cols = WINDOW_WIDTH // TILE_SIZE
   		rows = WINDOW_HEIGHT // TILE_SIZE

   		origin_offset = vector(
   			x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
   			y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE,)

   		self.support_surf.fill('green')


   		for col in range(cols + 1):
   			x = origin_offset.x + col * TILE_SIZE
   			pygame.draw.line(self.support_surf,LINE_COLOR,(x,0),(x,WINDOW_HEIGHT))

   		for row in range(rows + 1):
   			y = origin_offset.y + row * TILE_SIZE
   			pygame.draw.line(self.support_surf,LINE_COLOR,(0,y),(WINDOW_WIDTH,y))

   			self.display_surface.blit(self.support_surf,(0,0))



	def run(self, dt, event):
		self.event_loop(event)

		# drawing 
		self.display_surface.fill('black')

		pygame.draw.circle(self.display_surface,'red',self.origin,10)



