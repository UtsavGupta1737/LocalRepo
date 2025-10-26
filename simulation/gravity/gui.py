import pygame,sys
from pygame.locals import *
from setting import * 

pygame.init()

class BUTTON():
	def __init__(self,text = 'Text here',pos = (0,0),color = 'Black',topleft = False):
		self.text = str(text)
		self.pos = pos
		self.color = color
		self.topleft = topleft


	def draw(self,screen,text = 'Text here',pos = (0,0),color = 'Black',topleft = False):
		text = str(text)
		self.pos = pos
		self.color = color
		l = len(text)
		self.font = pygame.font.Font('freesansbold.ttf',30)
		self.surf = self.font.render(text,True,self.color)
		if self.topleft != True:
			self.surf_rect = self.surf.get_rect(center = self.pos)
		else:
			self.surf_rect = self.surf.get_rect(topleft = self.pos)

		screen.blit(self.surf,self.surf_rect)

	def click(self,event):
		if event.type == MOUSEBUTTONDOWN:
			if self.surf_rect.collidepoint(pygame.mouse.get_pos()):
				return True
		else:
			return False

	
# class TAB():
# 	def __init__(self):
# 		self.width = 150
# 		self.spacing = 5
# 		self.size = 50
# 		self.rect = None


# 	def create_data(self,target):
# 		for dic1 in data:
# 			if dic1['name'] == target:
# 				dic = dic1

# 		self.list = []
# 		for key in dic:
# 			s = str(key +' = '+ str(dic[key]))
# 			self.list.append(s)
# 		self.origin()


# 	def origin(self):
# 		l = len(self.list)
# 		self.height = (self.size*l) + (self.spacing*(l+1))
# 		self.rect = pygame.Rect((0,0),(self.width,self.height))
# 		self.rect.topleft = ((WINDOW_WIDTH - self.width),0)


# 	def draw(self,screen):
# 		pygame.draw.rect(screen,"White",self.rect)
# 		for i in range(len(self.list)):
# 			b = BUTTON()
# 			b.draw(screen,self.list[i],(700,0),True)
