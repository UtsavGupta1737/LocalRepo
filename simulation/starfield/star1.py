import pygame, random 
from settings import *
from pygame.locals import *

pygame.init()

class Star:
	def __init__(self):
		self.x = random.randrange(-width/2,width/2)
		self.y = random.randrange(-height/2,height/2)
		self.zx = random.randrange(1,width/2)
		self.zy = random.randrange(1,height/2)



	def reset(self):
		self.zx = random.randrange(1,width/2)
		self.zy = random.randrange(1,height/2)
		self.x = random.randrange(-width/2,width/2)
		self.y = random.randrange(-height/2,height/2)

	def update(self):
		self.zx -= 1
		self.zy -= 1
		if (self.zx <= 1 or self.zy <= 1):
			self.reset()



	def show(self, screen):
		sx = (self.x/self.zx)*width
		sy = (self.y/self.zy)*height

		r = (850/(self.zx + self.zy)) 
		# print('---------------------------------')
		# print((self.zx + self.zy))
		# print((850/(self.zx + self.zy)))
		# print(r)
		
		if(abs(sx) > width/2 or abs(sy) > height/2):
			self.reset()

		pygame.draw.ellipse(screen, 'white', (sx + width//2,sy + height//2,r,r))
		

	
