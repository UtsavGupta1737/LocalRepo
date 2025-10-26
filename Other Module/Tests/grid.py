# grid.set_grid(No. of Columns ,No. of Rows ,Cell Size ,Origin Point)
# In case of no setting default values are setted in settings file
# grid.display_surf(screen) ---> It draws grid on given Screen(Display)
# If no input is given it returns a surface with grid 


import pygame,sys
from pygame.locals import *
from settings import *

pygame.init()


class Grid():
	def __init__(self,col = COL,row = ROW,size = SIZE,origin = (0,0)):

		# default input from settings
		self.row = row
		self.col = col
		self.size = size
		self.origin = origin
		self.bg_color = LINE_BG_COLOR
		self.surf_width = self.col*self.size
		self.surf_height = self.row*self.size
		self.data =[[ 0 for i in range(self.col) ] for j in range(self.row)]

		
	# display surface or returns surface
	def display_grid(self,screen = None):
		if screen:
			# bliting on memory screen
			screen.blit(self.surf,self.origin)
		else:
			return self.surf


	# take input from user
	def set_grid(self,col,row,size,origin):

		# taking input from user
		self.row = row
		self.col = col
		self.size = size
		self.origin = origin
		self.surf = pygame.Surface((self.surf_width,self.surf_height))
		self.surf.fill(self.bg_color)
		self.draw_grid()

	
	# draw grid on the surface
	def draw_grid(self,surf = None):

		if surf: 
			self.surf = surf

		# thickness
		if self.size > 10 :thick = int(self.size/10)
		else: thick = 1

		# for colums
		for co in range(self.col+1):
			x = co*self.size 
			pygame.draw.line(self.surf,LINE_COLOR,(x,0),(x,self.surf_height),thick)

		# for rows
		for ro in range(self.row+1):
			y = ro*self.size 
			pygame.draw.line(self.surf,LINE_COLOR,(0,y),(self.surf_width,y),thick)

		if surf:
			return self.surf

	
	#Event Handling
	def event_hand(self,event):
		if pygame.key.get_pressed()[pygame.K_LCTRL]:
			print('yes')
		if pygame.key.get_pressed()[pygame.K_UP]:
			self.zoom(1)
		if pygame.key.get_pressed()[pygame.K_DOWN]:
			self.zoom(0)

	# def zoom(self,dir):
	# 	if dir == 1:
	# 		self.surf = pygame.transform.scale(self.surf,(500,500))
	# 	else:
	# 		self.size -= 10

	

	





	

		



