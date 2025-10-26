import pygame, random 
from settings import *
from pygame.locals import *

pygame.init()

class Star:
	def __init__(self):
		self.x = random.randrange(-width/2,width/2)
		self.y = random.randrange(-height/2,height/2)
		self.z = random.randrange(1,height)
		self.pz = self.z


	def reset(self):
		self.z = random.randrange(1,height)
		self.x = random.randrange(-width/2,width/2)
		self.y = random.randrange(-height/2,height/2)
		self.pz = self.z

	def update(self):

		speed = map(pygame.mouse.get_pos()[0], 0, width, 0, 10)

		self.z -= speed

		if (self.z <= 1):
			self.reset()



	def show(self, screen):
		# sx = (self.x/self.z)*width
		# sy = (self.y/self.z)*height

		sx = map(self.x/self.z, 0, 1, 0, width)
		sy = map(self.y/self.z, 0, 1, 0, width)


		r = 1000/(self.z)

		# r = map(self.z, 0, width, 30, 0)

		# px = (self.x/self.pz)*width
		# py = (self.y/self.pz)*height

		
		
		if(abs(sx) > width/2 or abs(sy) > height/2):
			self.reset()

		# pygame.draw.line(screen, 'white', (sx+width/2,sy+height/2),(px+width/2,py+height/2))
		pygame.draw.ellipse(screen, 'white', (sx + width//2,sy + height//2,r,r))
		

	
