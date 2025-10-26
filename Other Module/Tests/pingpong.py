import pygame ,sys 
from random import randint
from pygame.locals import *
from collison import *


pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

player = pygame.Rect(792,187,8,65)
ball = pygame.Rect(387,187,25,25)
ai = pygame.Rect(0,187,8,65)
spb = [randint(5,7),randint(2,4)]
spp = [20,0]
game_a = True
ai_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ai_timer,100)







def main(): 
	global game_a

	def move():
		ball.x += spb[0]
		ball.y += spb[1]


		

	def event_handling(event):

		if event.type == KEYDOWN and event.key == K_UP:
				player.y -= 20
		if event.type == KEYDOWN and event.key == K_DOWN:
			player.y += 20

		if event.type == KEYDOWN:
			print('*')
			game = True

		if event.type == ai_timer:
			ai_coll()



	def ai_coll():
		if ball.x < 750 and spb[0] < 0:
			
			aiy = ai.y +25
			if ball.y > aiy :
				ai.y += 10
			if ball.y < aiy:
				ai.y -= 10


	def bord():
		global game
		if ball.y > 375 or ball.y < 0:
			spb[1] *= -1
			if spb[0] > 0:
				spb[0] -= 0.1
			if spb[0] < 0:
				spb[0] += 0.1

		if ball.x > 800 or ball.x < 0:
			print('&')
			game = False
			ball.center = (400,200)
		

 		


	def cbr():
		if player.colliderect(ball) and spb[0] > 0:
			spb[0] *= -1
			spb[0] -= 0.15

			# print(ball.center[1])
			# print(player.center[1])
			# if ball.center[1] > player.center[1]:
			# 	spb[1] = abs(spb[1])
			# if ball.center[1] < player.center[1]:
			# 	spb[1] *= -1


		if ai.colliderect(ball) and spb[0] < 0:
			spb[0] *= -1
			print(spb)
			spb[0] += 0.15
			print(spb)
		



	
	while True:
		print(game_a)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit() 
			if game_a:
				event_handling(event)
			else:
				if event.type == KEYDOWN:
					game_a = True


		if game_a:
			screen.fill('Black')
			bord()
			cbr()
			move()

			pygame.draw.rect(screen,'White',player)
			pygame.draw.rect(screen,'White',ball)
			pygame.draw.rect(screen,'White',ai)
			pygame.draw.line(screen,"white",(400,0),(400,400),5)
			pygame.display.update()
			clock.tick(60)

		else:
			screen.fill('White')
			pygame.display.update()
			clock.tick(60)
			print(game)

if __name__ == '__main__':
	main()