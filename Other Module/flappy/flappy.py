import pygame,sys
from pygame.locals import *
from setting import *
from random import randint

pygame.init()

class BIRD:
	def __init__(self):
		self.height = 200 				# starting y  axis
		self.state = None				# Don't know
		self.g = -5						# Gravity
		self.bird = pygame.Rect(40,self.height,40,40) # Rectangles
		self.score = -1					# Initial Score
		self.hscore = 0 				# Don't know
			

	def display(self,screen,surf):		# display bird on screen
		self.bird.y = self.height
		screen.blit(surf,self.bird.topleft)

	def move(self):						# Gravity effect
		self.g += g
		self.height += self.g

	def jump(self):						# Jumping 
		self.g = -jump

	def event(self,event):				# Event Handling
		if event.type == MOUSEBUTTONDOWN:
			self.jump()
		if event.type == KEYDOWN and (event.key ==K_w or event.key == K_SPACE) :
			self.jump()

	def collision(self,pipe_list):		# Collision detection
		global game_active
		for pipe in pipe_list:
			if self.bird.colliderect(pipe.pipe_A) or self.bird.colliderect(pipe.pipe_B):
				game_active = False
			elif self.bird.bottom > 700 or self.bird.top < 0:
				game_active = False

	def reset(self):					# Reset the y level
		self.height = 200
		self.g = -5
		self.score = -1

	def up_score(self):					# Increase score
		if self.score == -1:
			return 0
		else:
			return self.score
	
	def get_score(self):				# Get last stored Score 
		score = file.read()
		self.hscore = int(score)
		




class PIPE():
	def __init__(self):
		self.speed = 4 					# Speed of pipe
		self.width = 100 				# Width of pipe 
		self.spacing = 175				# Spacing between them 
		self.free_pipe = None			# free Invisible pipe between two pipes 
		self.pipe_A = None				# Bottom pipe
		self.pipe_B = None				# Top pipe 
		self.create()					# Creates pipe

	def create(self):
		center = (WD_WIDTH + 25,randint(200,500))
		self.free_pipe = pygame.Rect(0,0,self.width,self.spacing)
		self.free_pipe.center = center

		self.pipe_A = pygame.Rect(0,0,self.width,600)
		self.pipe_A.x = self.free_pipe.x
		self.pipe_A.bottom = self.free_pipe.top
		
		self.pipe_B = pygame.Rect(0,0,self.width,600)
		self.pipe_B.x = self.free_pipe.x
		self.pipe_B.top = self.free_pipe.bottom

	def draw(self):	
		#pygame.draw.rect(screen,"Green",self.free_pipe,10)
		pygame.draw.rect(screen,"Red",self.pipe_A,10)
		pygame.draw.rect(screen,"Red",self.pipe_B,10)

	def move(self):
		self.free_pipe.x -= self.speed
		self.pipe_A.x -= self.speed
		self.pipe_B.x -= self.speed
		
	def img1(self,screen,surf):
		screen.blit(surf,(self.pipe_B.topleft))

	def img2(self,screen,surf):
		screen.blit(surf,(self.pipe_A.topleft))




class BUTTON():
	def __init__(self):
		pass

	def draw(self,text = 'Text here',pos = (0,0),color = None):
		text = str(text)
		l = len(text)
		self.font = pygame.font.Font('freesansbold.ttf',30)
		self.surf = self.font.render(text,True,'Black')
		self.surf_rect = self.surf.get_rect(center = pos)
		if color: self.surf.fill(color)
		screen.blit(self.surf,self.surf_rect)

	def click(self,event):
		if event.type == MOUSEBUTTONDOWN:
			if self.surf_rect.collidepoint(pygame.mouse.get_pos()):
				return True
		else:
			return False














# MAIN CODE
FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WD_WIDTH,WD_HEIGHT))
game_active = True


pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer,1500)
score_timer = pygame.USEREVENT + 1
pygame.time.set_timer(score_timer,2200)

back_surf = pygame.image.load('graphics/bg_5.png').convert_alpha()
pipe1_surf = pygame.image.load('graphics/pipe1.png').convert_alpha()
pipe2_surf = pygame.image.load('graphics/pipe2.png').convert_alpha()
bird_surf = pygame.image.load('graphics/bird.png').convert_alpha()

file = open('Data.txt','r')


flappy = BIRD()
flappy.get_score()
fps = BUTTON()
play = BUTTON()
sc = BUTTON()
hsc = BUTTON()

pipe_list = []




while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			file = open('Data.txt','w')
			print(flappy.hscore)
			file.write(str(flappy.hscore))
			file.close()
			pygame.quit()
			sys.exit()
		
		if game_active:
			flappy.event(event)

			if event.type == pipe_timer:
				pipe_list.append(PIPE())
			if event.type == score_timer:
				flappy.score += 1

		else:
			if play.click(event):
				flappy.reset()
				pipe_list = []			
				game_active = True

	if game_active:
		# DSIPLAY
		screen.fill('white')
		screen.blit(back_surf,(0,0))
		fps.draw(int(fpsClock.get_fps()),(20,15))

		for pipe in pipe_list:
			# pipe.draw()
			pipe.img1(screen,pipe1_surf,)
			pipe.img2(screen,pipe2_surf,)
		

		flappy.display(screen,bird_surf)

		# UPDATE
		flappy.collision(pipe_list)
		
		for pipe in pipe_list:
			pipe.move()
			pipe_list = [pipe for pipe in pipe_list if pipe.free_pipe.x > - 100]


		sc.draw(flappy.up_score(),(200,50))
		flappy.move()
	
	else:
		play.draw('RESTART',(200,350),)
		if flappy.score > flappy.hscore:
			flappy.hscore = flappy.score
		sc.draw(flappy.score,(200,50))

	

	
	hsc.draw('High Score : '+str(flappy.hscore),(200,20))
	pygame.display.update()
	fpsClock.tick(FPS)





