#import pygame and other necessary libraries
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *
import webbrowser
from globalvariables import GlobalVariables, gvar
from player import Player
#from trackgenerator import TrackGenerator
from road import Road
from laserbeam import Laserbeam

#initialize the source for global variables from import
global gvar

class KeyInput:
    """
    The 'KeyInput' class is used to handle user input from the keyboard.
    """
    def read(self):
        if gvar.INGAME == False:
            #user input
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #if any key is pressed on the start screen proceed to the car select screen
                    if gvar.FRAME == 1 and gvar.STARTSCREEN == True:
                        if event.key != (pygame.K_LSHIFT or pygame.K_RSHIFT):
                            gvar.FRAME = 2
                    #move left to change which car/course that will be selected
                    if event.key == pygame.K_LEFT:
                        if gvar.FRAME == 2:
                            if gvar.CARNUM > 1:
                                gvar.CARNUM -= 1
                        elif gvar.FRAME == 3:
                            if gvar.COURSENUM > 1:
                                gvar.COURSENUM -= 1
                    #move right to change which car/course that will be selected (within the bounds of what has been unlocked)
                    if event.key == pygame.K_RIGHT:
                        if gvar.FRAME == 2:
                            if gvar.GAMEDATA.count('1') < 6:
                                if gvar.CARNUM < 3:
                                    gvar.CARNUM += 1
                            elif gvar.GAMEDATA.count('1') >= 6:
                                if gvar.CARNUM < 4:
                                    gvar.CARNUM += 1
                        elif gvar.FRAME == 3:
                            if gvar.COURSENUM < (gvar.GAMEDATA.count('1')+1) and gvar.COURSENUM < 6:
                                gvar.COURSENUM += 1
                    #press enter to make your selection
                    if event.key == pygame.K_RETURN and gvar.STARTSCREEN == False:
                        #select car
                        if gvar.FRAME == 2:
                            gvar.FRAME = 3
                        #load the appropriate course background, create the game objects, reset car condition, start the mucis, and well, start the game!
                        elif gvar.FRAME == 3:
                            gvar.WINDOW = pygame.transform.scale(pygame.image.load('images/backgrounds/bg' + str(gvar.COURSENUM) + '.png'), (1000,302))
                            gvar.STREET = Road(gvar.COURSENUM)
                            gvar.RACER = Player(gvar.CARNUM, gvar.CARXSCALE/2, gvar.CARYSCALE/2, gvar.WIDTH/2, (7*gvar.HEIGHT/8-20-gvar.CARYADJUST/2))
                            gvar.LASERS = Laserbeam(gvar.COURSENUM)
                            gvar.CONDITION = 100
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/music' + str(gvar.COURSENUM) + '.mp3')
                            if gvar.PLAYMUSIC == True:
                                pygame.mixer.music.play(-1)
                            gvar.INGAME = True
                        #go back to car select frame and reset music to default if no new car has been unlocked
                        elif gvar.FRAME == 4:
                            #car unlocked scenario
                            if gvar.GAMEDATA.count('1') == 6:
                                gvar.GAMEDATA = '1111111'
                                file=open('data/gamedata/gamedata.txt','w+')
                                file.write(gvar.GAMEDATA)
                                file.close()
                                #new car unlocked frame
                                gvar.FRAME = 6
                            #typical scenario
                            else:
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load('music/music0.mp3')
                                pygame.mixer.music.play(-1)
                                gvar.FRAME = 2
                        #go back to car select frame and reset music to default
                        elif gvar.FRAME == 5 or gvar.FRAME == 6:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/music0.mp3')
                            pygame.mixer.music.play(-1)
                            gvar.FRAME = 2
                    #go back to the previous menu frame
                    if event.key == (pygame.K_LSHIFT or pygame.K_RSHIFT):
                        if gvar.FRAME == 2:
                            gvar.FRAME = 1
                            gvar.STARTSCREEN = True
                        elif gvar.FRAME == 3:
                            gvar.FRAME = 2
                    #reset game data
                    if event.key == pygame.K_r:
                        gvar.CARNUM = 1
                        gvar.COURSENUM = 1
                        file=open('data/gamedata/gamedata.txt','w+')
                        gvar.GAMEDATA = '0000000'
                        file.write(gvar.GAMEDATA)
                        file.close()
                    #toggle music on or off
                    if event.key == pygame.K_m:
                        if gvar.PLAYMUSIC == True:
                            pygame.mixer.music.stop()
                            gvar.PLAYMUSIC = False
                        else:
                            pygame.mixer.music.play(-1)
                            gvar.PLAYMUSIC = True
                    #open information file
                    if event.key == pygame.K_i:
                        webbrowser.open('https://github.com/sd2020spring/DepthProject-tolu-patrick/blob/master/README.md')
                    #play easter egg music
                    if event.key == pygame.K_l:
                        if gvar.GAMEDATA.count('1') >= 6:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/musicl.mp3')
                            pygame.mixer.music.play(1)
        else:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #player moves left when the left key is pressed and turning left image is set
                    if event.key == pygame.K_LEFT:
                        if gvar.CARNUM > 4:
                            gvar.RACER.dx = -9*(.001+gvar.STREET.speed)/gvar.CARNUM
                        else:
                            gvar.RACER.dx = -10*(.001+gvar.STREET.speed)/.75
                        gvar.RACER.image = gvar.RACER.imgleft
                    #player moves right when the right key is pressed and turning right image is set
                    if event.key == pygame.K_RIGHT:
                        if gvar.CARNUM > 4:
                            gvar.RACER.dx = 9*(.001+gvar.STREET.speed)/gvar.CARNUM
                        else:
                            gvar.RACER.dx = 10*(.001+gvar.STREET.speed)/.75
                        gvar.RACER.image = gvar.RACER.imgright
                    #player accelerates (the road progresses forward at a continuously increasing rate until max speed) when the up key is pressed
                    if event.key == pygame.K_UP:
                        if gvar.CARNUM != 4:
                            gvar.STREET.sp = .0003/gvar.CARNUM
                        elif gvar.CARNUM == 4:
                            gvar.STREET.sp = .0004
                    #player decelerates (the road progresses forward at a continuously decreasing rate until zero) when the down key is pressed
                    if event.key == pygame.K_DOWN:
                        gvar.STREET.sp = -.00035/gvar.CARNUM
                    #toggle music on or off
                    if event.key == pygame.K_m:
                        if gvar.PLAYMUSIC == True:
                            pygame.mixer.music.stop()
                            gvar.PLAYMUSIC = False
                        else:
                            pygame.mixer.music.play(-1)
                            gvar.PLAYMUSIC = True
                    #play easter egg music
                    if event.key == pygame.K_l:
                        if gvar.GAMEDATA.count('1') >= 6:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/musicl.mp3')
                            pygame.mixer.music.play(1)

                if event.type == pygame.KEYUP:
                    #player stops moving left
                    if event.key == pygame.K_LEFT:
                        gvar.RACER.dx = 0
                        gvar.RACER.image = gvar.RACER.img
                    #player stops moving right
                    if event.key == pygame.K_RIGHT:
                        gvar.RACER.dx = 0
                        gvar.RACER.image = gvar.RACER.img
                    #player stops accelerating
                    if event.key == pygame.K_UP:
                        gvar.STREET.sp = -.0001
                    #player stops decelerating as quickly
                    if event.key == pygame.K_DOWN:
                        gvar.STREET.sp = -.0001
