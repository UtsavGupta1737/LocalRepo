import pygame , sys
from pygame.locals import *

pygame.init()

def but():
    global t
    t = 20
    mo_re.y = 10
    mo_re.x = 255



def bounce():
    global sp_x,sp_y,ot_sp
    # moving mo_re
    mo_re.x += sp_x
    mo_re.y += sp_y

    collision_check()


    # moving and detecting other rect(ot_re)
    ot_re.y += ot_sp
    if ot_re.bottom >= sc_hi or ot_re.top <= 0:
        ot_sp *=-1
    cbr()
    draw()


def cbr():
    global sp_x,sp_y,ot_sp
    #collision between rectangles
    tol = 10#tolerance value
    if mo_re.colliderect(ot_re):
        if abs(ot_re.top-mo_re.bottom)>=tol:
            sp_y *= -1
        if abs(ot_re.bottom-mo_re.top)>=tol:
            print(sp_y)
            sp_y *= -1
            print(sp_y)
        if abs(ot_re.left-mo_re.right)<=tol:
            sp_x *= -1
        if abs(ot_re.right-mo_re.left)<=tol:
            sp_x *= -1
        

def draw():
    pygame.draw.rect(screen,(255,255,255),mo_re)
    pygame.draw.rect(screen,(255,0,0),ot_re)

def collision_check():
    global sp_x,sp_y,ot_sp
    #detecting border collosion
    if mo_re.right >= sc_wi or mo_re.left <= 0:
        sp_x *=-1
    elif mo_re.bottom >= sc_hi or mo_re.top <= 0:
        sp_y *=-1

def ground():  #true when collide with window boundry
    if mo_re.right >= sc_wi or mo_re.left <= 0:
        return True
    elif mo_re.bottom >= sc_hi or mo_re.top <= 0:
        return True
    else:
        return False



def grav (): #act as a gravity
    global t,sp_y
    if ground() == False:
        sp_y = (g*t)//2
        if ground() == True:
            t=0
        mo_re.y += sp_y

def mo_in():
    global po
    po = event.pos
    print(po)




FPS = 60
clock = pygame.time.Clock()

mox ,moy = 10,10
sc_wi ,sc_hi= 500 ,500
screen = pygame.display.set_mode((sc_wi,sc_hi))
mo_re = pygame.Rect(mox,moy,75,75)
sp_x ,sp_y = 5,5
ot_re = pygame.Rect(215,10,100,75)
ot_sp = 4
adg = 5
g ,t = 0.65,20
po = [35,35]
fontobj = pygame.font.Font('freesansbold.ttf',20)
textobj = fontobj.render('Reset',True,(255,0,0),(0,0,0))
re_se = textobj.get_rect()
re_se.topleft=(10,10)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.type == MOUSEMOTION:
                mo_in()
        if event.type == MOUSEBUTTONUP:
            if re_se.collidepoint(event.pos):
                but()





    screen.fill((0,0,0))
    screen.blit(textobj,re_se)
    bounce()

    pygame.display.update()
    t += 1
    clock.tick(FPS)







