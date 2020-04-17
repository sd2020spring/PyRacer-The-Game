import pygame, sys
from pygame.locals import *
import numpy as np
import random
import time
import datetime
from player import Player
from trackgenerator import TrackGenerator
from road import Road

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
    course = 0
    car = 1
    carfont = pygame.font.Font('fonts/Retron2000.ttf', 32)
    coursefont = pygame.font.Font('fonts/Retron2000.ttf', 48)
    ingamefontbig = pygame.font.Font('fonts/Retron2000.ttf', 32)
    ingamefontsmall = pygame.font.Font('fonts/Retron2000.ttf', 16)


    while True:
        if ingame == False:
            carimg ='images/player/front' + str(car) + '.png'
            menuslide = 'images/menuframes/frame' + str(frame) + '.png'
            bgimage = 'images/backgrounds/bg' + str(course) + '.png'
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
            if course == 0:
                coursename = 'PyRacer Speedway'
            elif course == 1:
                coursename = 'Countryside Backroads'
            elif course == 2:
                coursename = 'Tundra Expedition'
            elif course == 3:
                coursename = 'Desert Caravan'
            elif course == 4:
                coursename = 'City Outskirts'
            elif course == 5:
                coursename = 'Stellar Highway'

            cartitle = carfont.render(carname, True, WHITE, BLACK)
            coursetitle = coursefont.render(coursename, True, WHITE, BLACK)
            carrender = pygame.transform.scale(pygame.image.load(carimg), (carxscale,caryscale))
            DISPLAY.blit(window, (0,0))
            if frame == 2:
                DISPLAY.blit(carrender, (WIDTH/2-carxscale/2,HEIGHT/2-caryadjust))
                cartitlebox = cartitle.get_rect()
                cartitlebox.centerx = WIDTH/2
                cartitlebox.centery = HEIGHT/2-caryadjust-40
                DISPLAY.blit(cartitle, cartitlebox)
            if frame == 3:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if frame == 2:
                            car -= 1
                            if car <= 1:
                                car = 1
                        elif frame == 3:
                            course -= 1
                            if course <= 0:
                                course = 0
                    if event.key == pygame.K_RIGHT:
                        if frame == 2:
                            car += 1
                            if car >= 3:
                                car = 3
                        elif frame == 3:
                            course += 1
                            if course >= 5:
                                course = 5
                    if event.key == pygame.K_a:
                        if frame == 1:
                            frame = 2
                        elif frame == 2:
                            frame = 3
                        elif frame == 3:
                            window = pygame.transform.scale(pygame.image.load(bgimage), (1000,302))
                            street = Road(course)
                            racer = Player(car, 30, 30, WIDTH/2, 7*HEIGHT/8 - 20)
                            ingame = True
                    if event.key == pygame.K_b:
                        if frame == 2:
                            frame = 1
                        elif frame == 3:
                            frame = 2

        else:
            DISPLAY.blit(window, (0+2*street.tilt-100,0))
            speedtext = ingamefontbig.render((str(round((street.speed/6.9)*30000)) + ' km/h'), True, WHITE, BLACK)
            completiontext = ingamefontsmall.render('COMPLETION: ' + (str(round((street.distance/5))) + '%'), True, WHITE, BLACK)
            conditiontext = ingamefontsmall.render('CONDITION: ' + (str(round(100)) + ' %'), True, WHITE, BLACK)
            speedbox = speedtext.get_rect()
            speedbox.top = 10
            speedbox.left = 10
            completionbox = completiontext.get_rect()
            completionbox.top = 10
            completionbox.right = WIDTH-10
            conditionbox = conditiontext.get_rect()
            conditionbox.top = 40
            conditionbox.right = WIDTH-10

            street.readtrack()
            street.update()
            racer.move()

            if car == 2:
                if street.speed > .05:
                    street.speed = .049
            if car == 3:
                if street.speed > .04:
                    street.speed = .039

            if street.accelerate:
                if street.tilt == 0:
                    racer.dxs = 0
                elif street.tilt == -1:
                    racer.dxs = 2*((street.speed+.3)*5)
                elif street.tilt == 1:
                    racer.dxs = -2*((street.speed+.3)*5)
            else:
                racer.dxs = 0

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #player moves left when left key is pressed
                    if event.key == pygame.K_LEFT:
                        racer.dx = -5
                        racer.image = racer.imgleft
                    #player moves right when right key is pressed
                    if event.key == pygame.K_RIGHT:
                        racer.dx = 5
                        racer.image = racer.imgright
                    #player moves up when up key is pressed
                    if event.key == pygame.K_UP:
                        street.accelerate = True
                        street.sp = .0005/car
                    #player moves down when down key is pressed
                    if event.key == pygame.K_DOWN:
                        street.sp = -.001/car

                if event.type == pygame.KEYUP:
                    #player stops moving left
                    if event.key == pygame.K_LEFT:
                        racer.dx = 0
                        racer.image = racer.img
                    #player stops moving right
                    if event.key == pygame.K_RIGHT:
                        racer.dx = 0
                        racer.image = racer.img
                    #player stops moving up
                    if event.key == pygame.K_UP:
                        street.accelerate = False
                        street.sp = -.001
                    #player stops moving down
                    if event.key == pygame.K_DOWN:
                        street.sp = 0

            DISPLAY.blit(racer.image, (racer.x,racer.y-caryadjust/2))
            DISPLAY.blit(speedtext, speedbox)
            DISPLAY.blit(completiontext, completionbox)
            DISPLAY.blit(conditiontext, conditionbox)

        #the following line continously calls the while loop
        pygame.display.update()

#the following line calls the main function and starts the game
main()
