import pygame, sys
from pygame.locals import *
import numpy as np
import random
import time
import datetime
from player import Player
from trackgenerator import TrackGenerator
from road import Road
from laserbeam import Laserbeam

WIDTH = 800
HEIGHT = 500

def main():
    pygame.init()
    pygame.display.set_caption('PyRacer')
    tilt = 0
    trackgen = TrackGenerator()
    trackgen.generate()
    ingame = False
    DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    DISPLAY.fill(BLACK)
    frame = 1
    course = 1
    car = 1
    startscreen = True
    condition = 100
    carfont = pygame.font.Font('fonts/Retron2000.ttf', 32)
    coursefont = pygame.font.Font('fonts/Retron2000.ttf', 48)
    ingamefontbig = pygame.font.Font('fonts/Retron2000.ttf', 32)
    ingamefontsmall = pygame.font.Font('fonts/Retron2000.ttf', 16)
    pygame.mixer.music.load('music/music0.mp3')
    pygame.mixer.music.play(-1)
    filename = 'data/gamedata.txt'
    with open(filename) as file:
        gamedata = file.readline()
    file.close()

    while True:
        if ingame == False:
            if frame > 1:
                startscreen = False
            carimg ='images/player/front' + str(car) + '.png'
            menuslide = 'images/menuframes/frame' + str(frame) + '.png'
            bgimage = 'images/backgrounds/bg' + str(course) + '.png'
            turboimg ='images/objects/goldenturbo.png'
            window = pygame.transform.scale(pygame.image.load(menuslide), (800,500))

            if car == 1:
                carxscale = 232
                caryscale = 128
                caryadjust = 0
                carname = 'Sprinter'
            elif car == 2:
                carxscale = 232
                caryscale = 173
                caryadjust = 45
                carname = 'Sport-Utility'
            elif car == 3:
                carxscale = 282
                caryscale = 246
                caryadjust = 118
                carname = 'Big Rig'
            elif car == 4:
                carxscale = 244
                caryscale = 128
                caryadjust = 0
                carname = 'GOLDEN ESPRIT'

            if course == 1:
                coursename = 'PyRacer Speedway'
            elif course == 2:
                coursename = 'Countryside Backroads'
            elif course == 3:
                coursename = 'Tundra Expedition'
            elif course == 4:
                coursename = 'Desert Caravan'
            elif course == 5:
                coursename = 'City Outskirts'
            elif course == 6:
                coursename = 'Stellar Highway'

            cartitle = carfont.render(carname, True, WHITE, BLACK)
            coursetitle = coursefont.render(coursename, True, WHITE, BLACK)
            carrender = pygame.transform.scale(pygame.image.load(carimg), (carxscale,caryscale))
            turborender = pygame.transform.scale(pygame.image.load(turboimg), (50,50))
            DISPLAY.blit(window, (0,0))
            if frame == 2:
                DISPLAY.blit(carrender, (WIDTH/2-carxscale/2,HEIGHT/2-caryadjust))
                for i in range(gamedata.count('1')):
                    DISPLAY.blit(turborender, ((WIDTH/2+12.5)-((3-i)*75),385))
                cartitlebox = cartitle.get_rect()
                cartitlebox.centerx = WIDTH/2
                cartitlebox.centery = HEIGHT/2-caryadjust-40
                DISPLAY.blit(cartitle, cartitlebox)
            elif frame == 3:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            elif frame == 4:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            elif frame == 5:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if frame == 1 and startscreen == True:
                        if event.key != (pygame.K_LSHIFT or pygame.K_RSHIFT):
                            frame = 2
                    if event.key == pygame.K_LEFT:
                        if frame == 2:
                            if car > 1:
                                car -= 1
                        elif frame == 3:
                            if course > 1:
                                course -= 1
                    if event.key == pygame.K_RIGHT:
                        if frame == 2:
                            if gamedata.count('1') < 6:
                                if car < 3:
                                    car += 1
                            elif gamedata.count('1') >= 6:
                                if car < 4:
                                    car += 1
                        elif frame == 3:
                            if course < (gamedata.count('1')+1) and course < 6:
                                course += 1
                    if event.key == pygame.K_RETURN and startscreen == False:
                        if frame == 2:
                            frame = 3
                        elif frame == 3:
                            window = pygame.transform.scale(pygame.image.load(bgimage), (1000,302))
                            street = Road(course)
                            racer = Player(car, 30, 30, WIDTH/2, 7*HEIGHT/8 - 20)
                            lasers = Laserbeam(course)
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/music' + str(course) + '.mp3')
                            pygame.mixer.music.play(-1)
                            ingame = True
                        elif frame == 4 or frame == 5:
                            frame = 2
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/music0.mp3')
                            pygame.mixer.music.play(-1)
                    if event.key == (pygame.K_LSHIFT or pygame.K_RSHIFT):
                        if frame == 2:
                            frame = 1
                            startscreen = True
                        elif frame == 3:
                            frame = 2
                    if event.key == (pygame.K_r):
                        file=open('data/gamedata.txt','w+')
                        gamedata = '000000'
                        file.write('000000')
                        file.close()

        else:
            DISPLAY.blit(window, (0+2*street.tilt-100,0))
            speedtext = ingamefontbig.render((str(round((street.speed/6.9)*25000)) + ' km/h'), True, WHITE, BLACK)
            completiontext = ingamefontsmall.render('[COMPLETION: ' + (str(round((street.distance/len(street.trackroad))*100)) + '% ] [LAP ' + str(street.lapnum) + '/3]'), True, WHITE, BLACK)
            conditiontext = ingamefontsmall.render('CONDITION: ' + (str(round(condition)) + ' %'), True, WHITE, BLACK)
            speedbox = speedtext.get_rect()
            speedbox.top = 10
            speedbox.left = 10
            completionbox = completiontext.get_rect()
            completionbox.top = 10
            completionbox.right = WIDTH-10
            conditionbox = conditiontext.get_rect()
            conditionbox.top = 40
            conditionbox.right = WIDTH-10

            lasers.update()
            street.readtrack()
            street.update()
            racer.move()

            if car == 2:
                if street.speed > .07:
                    street.speed = .069
            if car == 3:
                if street.speed > .06:
                    street.speed = .059

            if street.accelerate:
                if street.tilt == 0:
                    racer.dxs = 0
                elif street.tilt == -1:
                    racer.dxs = 2*(street.speed+.001)
                elif street.tilt == 1:
                    racer.dxs = -2*(street.speed+.001)
            else:
                racer.dxs = 0

            if ((racer.x-(carxscale/4) >= lasers.x1-40 and racer.x-(carxscale/4) <= lasers.x1+40 and lasers.y1 > -(500-racer.y+(caryadjust/2)))
                or (racer.x-(carxscale/4) >= lasers.x2-40 and racer.x-(carxscale/4) <= lasers.x2+40 and lasers.y2 > -(500-racer.y+(caryadjust/2)))
                or (racer.x-(carxscale/4) >= lasers.x3-40 and racer.x-(carxscale/4) <= lasers.x3+40 and lasers.y3 > -(500-racer.y+(caryadjust/2)))
                or (racer.x+(carxscale/4) >= lasers.x1-40 and racer.x+(carxscale/4) <= lasers.x1+40 and lasers.y1 > -(500-racer.y+(caryadjust/2)))
                or (racer.x+(carxscale/4) >= lasers.x2-40 and racer.x+(carxscale/4) <= lasers.x2+40 and lasers.y2 > -(500-racer.y+(caryadjust/2)))
                or (racer.x+(carxscale/4) >= lasers.x3-40 and racer.x+(carxscale/4) <= lasers.x3+40 and lasers.y3 > -(500-racer.y+(caryadjust/2)))):
                condition -= .2/car

            if (round((street.distance/len(street.trackroad))*100) >= 100 and street.lapnum >= 3):
                ingame = False
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/musicc.mp3')
                pygame.mixer.music.play(-1)
                gamedata = gamedata[:(course-1)] + '1' + gamedata[(course):]
                file=open('data/gamedata.txt','w+')
                file.write(gamedata)
                file.close()
                frame = 4

            if (round(condition) <= 0):
                ingame = False
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/musicf.mp3')
                pygame.mixer.music.play(-1)
                frame = 5

            for gameevent in pygame.event.get():
                if gameevent.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if gameevent.type == pygame.KEYDOWN:
                    #player moves left when left key is pressed
                    if gameevent.key == pygame.K_LEFT:
                        racer.dx = -10*(.001+street.speed)
                        racer.image = racer.imgleft
                    #player moves right when right key is pressed
                    if gameevent.key == pygame.K_RIGHT:
                        racer.dx = 10*(.001+street.speed)
                        racer.image = racer.imgright
                    #player moves up when up key is pressed
                    if gameevent.key == pygame.K_UP:
                        street.accelerate = True
                        if car != 4:
                            street.sp = .0005/car
                        elif car == 4:
                            street.sp = .0006
                    #player moves down when down key is pressed
                    if gameevent.key == pygame.K_DOWN:
                        street.sp = -.001/car

                if gameevent.type == pygame.KEYUP:
                    #player stops moving left
                    if gameevent.key == pygame.K_LEFT:
                        racer.dx = 0
                        racer.image = racer.img
                    #player stops moving right
                    if gameevent.key == pygame.K_RIGHT:
                        racer.dx = 0
                        racer.image = racer.img
                    #player stops moving up
                    if gameevent.key == pygame.K_UP:
                        street.accelerate = False
                        street.sp = -.0002
                    #player stops moving down
                    if gameevent.key == pygame.K_DOWN:
                        street.sp = 0

            DISPLAY.blit(racer.image, (racer.x,racer.y-caryadjust/2))
            DISPLAY.blit(lasers.image, (lasers.x1,lasers.y1))
            DISPLAY.blit(lasers.image, (lasers.x2,lasers.y2))
            DISPLAY.blit(lasers.image, (lasers.x3,lasers.y3))
            DISPLAY.blit(speedtext, speedbox)
            DISPLAY.blit(completiontext, completionbox)
            DISPLAY.blit(conditiontext, conditionbox)

        #the following line continously calls the while loop
        pygame.display.update()

#the following line calls the main function and starts the game
main()
