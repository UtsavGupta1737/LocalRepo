import pygame,sys,math
from pygame.locals import *
from pygame.math import Vector2 as vector


class Vector:
	def __init__(self):
		self.origin = (500,350)
		self.vector = vector(10,-10)

	def draw(self,screen):
		pygame.draw.line(screen,'White',self.origin,(self.vector + self.origin))
