import pygame ,sys
from pygame.locals import *
from random import randint




def clou_anime(clou_list):
    if clou_list:
        for clou_rect in clou_list:
            clou_rect.x -= 5
            #screen.blit(build_surf,clou_rect)
            screen.blit(clou_surf,clou_rect)

        clou_list = [clou for clou in clou_list if clou.x > -200]
        return clou_list
    else:
        return[]

def grav():
    global g
    g += 1
    play_rect.bottom +=g

def score():

    global fps_rect
    current_time = int((pygame.time.get_ticks() -start_time) //1000)
    font_obj = pygame.font.Font('freesansbold.ttf',20)
    score_surf = font_obj.render('Score '+str(current_time),True,(0,0,0))
    score_rect = score_surf.get_rect()
    score_rect.center = (380,20)
    screen.blit(score_surf,score_rect)
    fps = font_obj.render('FPS = '+str(int(clock.get_fps())),True,'Black')
    fps_rect = fps.get_rect(topleft = (0,5))
    screen.blit(fps,fps_rect)

    return current_time

def obstacle_move(obstacle_list):
    if obstacle_list:
        for obstacle_rec in obstacle_list:
            obstacle_rec.x -= 8
            if obstacle_rec.bottom == 300:screen.blit(snail_surf,obstacle_rec)
            else:screen.blit(fly_surf,obstacle_rec)


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -50]
        return obstacle_list
    else:
        return []

def collision(player,obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect):
                return False
    return True




pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,400))
game_active = False
start_time = 0
g = 0
hscore ,lscore= 0,0
cheat = False


#TEXT
font_obj = pygame.font.Font('freesansbold.ttf',36)
game_name = font_obj.render('Alien Running',True,'Cyan')
game_name_rect = game_name.get_rect(center = (400,20))
instr = font_obj.render('Press SPACE To Start The Game',True,'Cyan')
instr_rect = instr.get_rect(center = (400,375))

#SKY
sky_surf = pygame.image.load('image/back1.png').convert_alpha()

#CLOUDS AND BUILDINGS
clou_surf = pygame.image.load('image/cloud.png').convert_alpha()
#build_surf = pygame.image.load('image/buildings.png').convert_alpha()
clou_rect_list = []

#GROUND
grou_surf = pygame.image.load('image/grou.png').convert_alpha()

#PLAYER
play_surf = pygame.image.load('image/char.png').convert_alpha()
play_rect = play_surf.get_rect()
play_rect.bottomleft = (10,300)

#for intro screen
playin_surf = pygame.image.load('image/charin.png').convert_alpha()
playin_surf = pygame.transform.scale(playin_surf,(300,300))
playin_rect = playin_surf.get_rect(center = (400,200))

#OBSTACLES
#snail
snail_surf = pygame.image.load('image/snail.png').convert_alpha()
#fly
fly_surf = pygame.image.load('image/fly.png').convert_alpha()

#...
obstacle_rec_list = []

#TIMER
obstacle_timer = pygame.USEREVENT + 1
cloud_timer = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_timer,700)
pygame.time.set_timer(cloud_timer,1000)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if play_rect.bottom == 300:
                if event.type == KEYDOWN and (event.key ==K_w or event.key == K_SPACE ):
                    g = -15
                if event.type == MOUSEBUTTONDOWN:
                    g = -15
                    if fps_rect.collidepoint(event.pos):
                        if cheat:
                            cheat = False
                        else:
                            cheat = True
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rec_list.append(snail_surf.get_rect(bottomleft = (randint(900,1100),300)))
                else:
                    obstacle_rec_list.append(fly_surf.get_rect(bottomleft = (randint(900,1100),210)))
            if event.type == cloud_timer:
                clou_rect_list.append(clou_surf.get_rect(center = (900,randint(50,75))))
                #clou_rect_list.append(build_surf.get_rect(bottomleft = (0,303)))

        else:
            if event.type == KEYDOWN and (event.key ==K_w or event.key == K_SPACE):
                game_active = True
            if event.type == MOUSEBUTTONDOWN:
                game_active = True
            start_time = pygame.time.get_ticks()



    if game_active:

        screen.fill('Black')

        #BACKGROUND
        screen.blit(sky_surf,(0,0))
        screen.blit(grou_surf,(0,300))

        #CLOUDS
        clou_rect_list = clou_anime(clou_rect_list)

        #TEXT
        lscore = score()

        #PLAYER
        grav()
        if play_rect.bottom>300:
            play_rect.bottom = 300
        screen.blit(play_surf,play_rect)

        #OBSTACLES
        obstacle_rec_list = obstacle_move(obstacle_rec_list)
        #COLLISION
        game_active = collision(play_rect,obstacle_rec_list)

        #CHEAT
        if cheat:
            if obstacle_rec_list:
                for obstacle_rect in obstacle_rec_list:
                    if obstacle_rect.bottom > 290 and obstacle_rect.x < play_rect.right+40 and play_rect.bottom == 300:
                        g = -10



    else:
        screen.fill((75,75,75))
        screen.blit(playin_surf,playin_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(instr,instr_rect)
        if lscore > hscore:
            hscore = lscore
        hi_score = font_obj.render('High Score = '+str(hscore),True,('Cyan'))
        hi_sc_rect = hi_score.get_rect(center = (400,50))
        screen.blit(hi_score,hi_sc_rect)
        obstacle_rec_list.clear()
        clou_rect_list.clear()
        play_rect.bottom = 300
                            

    pygame.display.update()
    clock.tick(60)






