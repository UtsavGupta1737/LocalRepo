import pygame ,sys
from pygame.locals import *
from random import randint


def move(rec1,rec2,sp1,sp2):
	rec1.x += sp1[0]
	rec1.y += sp1[1]
	rec2.x += sp2[0]
	rec2.y += sp2[1]

def bord(rec1,rec2,sp1,sp2):
	if rec1.right > 400 or rec1.left < 0:
		sp1[0] *= -1
	if rec1.bottom > 400 or rec1.top < 0:
		sp1[1] *= -1
	if rec2.right > 400 or rec2.left < 0:
		sp2[0] *= -1
	if rec2.bottom > 400 or rec2.top < 0:
		sp2[1] *= -1

def cbr(rec1,rec2,sp1,sp2):
	if rec1.colliderect(rec2):
		tol = 10
		if abs(rec2.top-rec1.bottom) < tol and sp1[1]>0:
			sp1[1] *= -1

		if abs(rec2.bottom-rec1.top) < tol and sp1[1]<0:
			sp1[1] *= -1

		if abs(rec2.left-rec1.right) < tol and sp1[0]>0:
			sp1[0] *= -1

		if abs(rec2.right-rec1.left) < tol and sp1[0]<0:
			sp1[0] *= -1




def main():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((400,400))
	rec1 = pygame.Rect(10,300,50,50)
	sp1 = [1,2]
	rec2 = pygame.Rect(15,150,50,50)
	sp2 = [2,2]


	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		screen.fill('Black')
		bord(rec1,rec2,sp1,sp2)
		cbr(rec1,rec2,sp1,sp2)
		cbr(rec2,rec1,sp2,sp1)
		move(rec1,rec2,sp1,sp2)
		
		pygame.draw.rect(screen,'Red',rec1)
		pygame.draw.rect(screen,'cyan',rec2)

		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__' :
	main()