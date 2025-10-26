import pygame,sys,setting,math,time
from pygame.locals import *
from setting import * 
from gui import *
from pygame.math import Vector2 as vector

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
Grav = True

class BODY():
	def __init__(self):
		self.name = ''
		self.mass = 10**10
		self.radius = None
		self.v = vector()
		self.a = vector()
		self.trail = []



	def init(self,data):
		self.name = data['name']
		self.mass = data['mass']
		self.color = data['color']
		self.radius = data['radius']
		self.center = vector(data['center'])
		self.v = vector(data['v'])
		self.colrect = Rect(0,0,self.radius,self.radius)
		self.trail = [(self.center.x,self.center.y)]


	def draw(self,surface):
		pygame.draw.aalines(surface,self.color,False,self.trail,1000)
		pygame.draw.circle(surface,self.color,self.center,self.radius)
		pygame.draw.rect(surface,'White',self.colrect)
		


	def move(self,dt):
		self.v += self.a
		self.center += self.v
		self.trail.append((self.center.x,self.center.y))
		self.clear()
		self.colrect.center = self.center


	def gravityf(self,body):
		# print(self.name)
		# print(' to ')
		# print(body.name)



		rv = body.center - self.center
		r = rv.magnitude_squared()

		rv2 = rv.normalize()
		
		mass = self.mass * body.mass 

		f = (6.6*10**-11 * mass) / r
		f = rv2 * f
		self.a = f / self.mass

		# print(f)
		

	def clear(self):
		l = len(self.trail)
		if l > self.radius * 10:		
			self.trail.pop(0)




sun = BODY()
earth = BODY()
mars = BODY()
moon = BODY()








earth_data = {'name':'earth','mass':10**6,'color':'Blue','radius':50,'center':(800,350),'v':(0,00.12)}
mars_data = {'name':'mars','mass':1.1*10**5,'color':'Red','radius':40,'center':(300,350),'v':(0.2,0.1)}
sun_data = {'name':'sun','mass':3.33*10**11,'color':'Yellow','radius':50,'center':(500,350),'v':(0,0)}
moon_data = {'name':'moon','mass':0.012,'color':'Gray','radius':10,'center':(850,350),'v':(0,0.1)}

grav = BUTTON()
fps = BUTTON()




sun.init(sun_data)
earth.init(earth_data)
mars.init(mars_data)
moon.init(moon_data)
bodys = [sun,earth,moon,mars]


pt = time.time()

while True:
	dt = time.time() - pt
	pt = time.time()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if grav.click(event):
				if Grav:
					Grav = False
				else:
					Grav = True



	screen.fill('black')
	
	
	for body in bodys:
		for body1 in bodys:
			if body != body1:
				if Grav:
					
					body.gravityf(body1)
				body.move(dt)
		

		
		body.draw(screen)


	grav.draw(screen,'GRAVITY',(70,15),'Cyan')
	fps.draw(screen,int(clock.get_fps()),(50,50),'White')
	

	


	clock.tick(100)
	pygame.display.update()


