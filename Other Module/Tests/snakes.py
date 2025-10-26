import pygame ,sys 
from random import randint
from pygame.locals import *
from pygame.math import Vector2 

class FRUIT():
	def __init__(self):
		#random
		self.randomise()

	def draw_fruit(self):
		self.rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
		screen.blit(apple,self.rect)
		#pygame.draw.rect(screen,'Red',self.rect)

	def randomise(self):
		self.x = randint(0,cell_number-1)
		self.y = randint(0,cell_number-1)
		self.pos = Vector2(self.x,self.y)
		

class SNAKE():
	def __init__(self):
		self.body = [Vector2(9,10),Vector2(8,10),Vector2(7,10)]
		self.direction = Vector2(1,0)
		self.new_block = False

		self.crunch_sound = pygame.mixer.Sound('graphics/crunch.wav')

	def draw(self):
		for block in self.body:
			self.rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
			pygame.draw.rect(screen,'Blue',self.rect)

	def move_snake(self):
		if self.new_block:
			body_copy = self.body[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
		body_copy.insert(0,body_copy[0] + self.direction)
		self.body = body_copy[:]

	def add_block(self):
		#add new block
		self.new_block = True

	def play_crunch_sound(self):
		#play crunch sound
		self.crunch_sound.play()


class MAIN():
	def __init__(self):
		self.fruit = FRUIT()
		self.snake = SNAKE()

	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()

	def draw_elements(self):
		self.draw_grass()
		self.fruit.draw_fruit()
		self.snake.draw()
		self.draw_score()

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomise()
			self.snake.add_block()
			#self.snake.play_crunch_sound()

	def check_fail(self):
		if not 0 <= self.snake.body[0].x < cell_number:
			self.game_over()
		if not 0 <= self.snake.body[0].y < cell_number:			 	
			self.game_over()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()

	def game_over(self):
		pygame.quit()
		sys.exit()

	def draw_grass(self):
		grass_color = ('Black')

		for row in range(cell_number):
			if row % 2 == 0:
				for col in range(cell_number):
					if col % 2 == 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)	
						pygame.draw.rect(screen,grass_color,grass_rect)	

			else:	
				for col in range(cell_number):
					if col % 2 != 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)	
						pygame.draw.rect(screen,grass_color,grass_rect)
				
	def draw_score(self):
		score_text = str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text,False,(56,75,12))
		bg_rect = pygame.Rect(((cell_size*cell_number)/2)-5,30,23,50)

		screen.blit(score_surface,((cell_size*cell_number)/2,50))
		screen.blit(apple,(((cell_size*cell_number)/2)-1,35))
		pygame.draw.rect(screen,('Black'),bg_rect,2)



pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
FPS = 60
cell_size = 15
cell_number = 30
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

apple = pygame.image.load('graphics/apple.png').convert_alpha()
game_font = pygame.font.Font(None,35)


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		if event.type == KEYDOWN:
			if event.key == K_w and main_game.snake.direction != Vector2(0,1):
				main_game.snake.direction = Vector2(0,-1)
			if event.key == K_a and main_game.snake.direction != Vector2(1,0):
				main_game.snake.direction = Vector2(-1,0)
			if event.key == K_s and main_game.snake.direction != Vector2(0,-1):
				main_game.snake.direction = Vector2(0,1)
			if event.key == K_d and main_game.snake.direction != Vector2(-1,0):
				main_game.snake.direction = Vector2(1,0)




	screen.fill('White')
	main_game.draw_elements()
	pygame.display.update()
	clock.tick(FPS)