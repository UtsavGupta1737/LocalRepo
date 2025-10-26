import pygame,math,random
from pygame.locals import *
from settings import *
from pygame.math import Vector2 as vector
from pygame.key import get_pressed as key_pressed 

pygame.init()

class Snake():
	def __init__(self):

		self.len = 1 #Size of Snake 
		self.body = []	# List to store the body pos 
		self.pos = vector()		#Head postion of Snake
		self.vel = vector(0,1)
		self.food = Rect(100,100,tile,tile)
		self.body.append(self.pos)
		self.ppos = vector() # to store previous location of head

	def update(self):
		
		self.ppos.x,self.ppos.y = self.pos.x,self.pos.y	# storing only values 
		self.pos += self.vel * tile

		rec = Rect(self.pos.x, self.pos.y, tile, tile)  # for collision detection 
		if(rec.colliderect(self.food)):	# It need a rectangle
			self.eat()
		else:
			self.move_body()	#only move whem not eating

	def show(self,screen):

		pygame.draw.ellipse(screen, 'red', self.food)

		for body in self.body:
			rec =  Rect(body.x, body.y ,tile,tile)
			pygame.draw.rect(screen, 'white', rec)

	def move_body(self):

		i = 1
		while(i < self.len-1):		# moving the body
			self.body[i].x,self.body[i].y = self.body[i+1].x,self.body[i+1].y
			i += 1

		if self.len > 1:			# moving the eye part sepearately
			self.body[self.len - 1].x,self.body[self.len - 1].y = self.ppos.x,self.ppos.y

	def input(self, event):

		cooldown = False

		if event.type == pygame.KEYDOWN:
			if(event.key == pygame.K_a and self.vel.x != 1):
				self.vel = vector(-1,0)
			elif(event.key == pygame.K_d and self.vel.x != -1):
				self.vel = vector(1,0)
			elif(event.key == pygame.K_w and self.vel.y != 1):
				self.vel = vector(0,-1)
			elif(event.key == pygame.K_s and self.vel.y != -1):
				self.vel = vector(0,1)
	
	def eat(self):
		self.food = Rect((random.randint(0,width//tile-1)*tile,random.randint(0,height//tile-1)*tile),( tile, tile))

		self.len += 1

		self.body.append(vector(self.ppos))


