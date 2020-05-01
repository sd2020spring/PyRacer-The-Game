#import pygame, local class files, and other necessary libraries
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *
import webbrowser
from globalvariables import GlobalVariables, gvar
from keyinput import KeyInput
from player import Player
#from trackgenerator import TrackGenerator
from road import Road
from laserbeam import Laserbeam

#initialize the source for global variables from import
global gvar

#set default display dimensions and create a display to render the game, alongside some colors for text display
WIDTH = gvar.WIDTH
HEIGHT = gvar.HEIGHT
DISPLAY = gvar.DISPLAY
WHITE = (255, 255, 255)
BLACK = (0,0,0)
DISPLAY.fill(BLACK)

def main():
    """
	The 'main()' function is used to run the game, manage which objects render, and play music,
    along with saving data and pulling data to be read by the objects that need it.

	First all the objects are initialized and then in the following while loop all of the interactions
	(from user input, to collision detection, to the head-up display and UI) are handled.
	"""
    #setup pygame window
    pygame.init()
    pygame.display.set_caption('PyRacer')
    #trackgen = TrackGenerator() <- if you want to create new tracks uncomment this...
    #trackgen.generate() <- ...and this
    #define the different fonts that will be used
    carfont = pygame.font.Font('fonts/Retron2000.ttf', 32)
    coursefont = pygame.font.Font('fonts/Retron2000.ttf', 48)
    ingamefontbig = pygame.font.Font('fonts/Retron2000.ttf', 32)
    ingamefontsmall = pygame.font.Font('fonts/Retron2000.ttf', 16)
    #load the default music and play continuously
    pygame.mixer.music.load('music/music0.mp3')
    pygame.mixer.music.play(-1)
    #initialize keyboard input object
    keyreader = KeyInput()

    while True:
        """
		As mentioned before this loop handeles all of the interactions.

		Although dispersed, this while loop can be split into three overall concepts:
		Graphics Rendering, User Input, and Collision Detection.

        Two of the three concepts are presented in the 'ingame == False' statement while
        all three are presented in the 'ingame == True' statement.
		"""
        #things happening during the out-of-game scenario
        if gvar.INGAME == False:
            #graphics rendering
            #if the menu frame is past the first one, we are no longer on the start screen (this is used to prevent a bug when going back to the start screen)
            if gvar.FRAME > 1:
                gvar.STARTSCREEN = False
            #depending on the current car value the image scaling, y-axis adujust for centering, and listed name will change
            if gvar.CARNUM == 1:
                gvar.CARXSCALE = 232
                gvar.CARYSCALE = 128
                gvar.CARYADJUST = 0
                carname = 'Sprinter'
            elif gvar.CARNUM == 2:
                gvar.CARXSCALE = 232
                gvar.CARYSCALE = 173
                gvar.CARYADJUST = 45
                carname = 'Sport-Utility'
            elif gvar.CARNUM == 3:
                gvar.CARXSCALE = 282
                gvar.CARYSCALE = 246
                gvar.CARYADJUST = 118
                carname = 'Big Rig'
            elif gvar.CARNUM == 4:
                gvar.CARXSCALE = 244
                gvar.CARYSCALE = 128
                gvar.CARYADJUST = 0
                carname = 'GOLDEN ESPRIT'
            #depending on the current course value the listed name will change
            if gvar.COURSENUM == 1:
                coursename = 'PyRacer Speedway'
            elif gvar.COURSENUM == 2:
                coursename = 'Countryside Backroads'
            elif gvar.COURSENUM == 3:
                coursename = 'Tundra Expedition'
            elif gvar.COURSENUM == 4:
                coursename = 'Desert Caravan'
            elif gvar.COURSENUM == 5:
                coursename = 'City Outskirts'
            elif gvar.COURSENUM == 6:
                coursename = 'Stellar Highway'
            #load the source image representing the out-of-game frame the menu is on
            gvar.WINDOW = pygame.transform.scale(pygame.image.load('images/menuframes/frame' + str(gvar.FRAME) + '.png'), (800,500))
            #create pygame surface to render car name text (black background with white text)
            cartitle = carfont.render(carname, True, WHITE, BLACK)
            #create pygame surface to render course name text (black background with white text)
            coursetitle = coursefont.render(coursename, True, WHITE, BLACK)
            #load the source image representing the car in the car select screen
            carrender = pygame.transform.scale(pygame.image.load('images/player/front' + str(gvar.CARNUM) + '.png'), (gvar.CARXSCALE,gvar.CARYSCALE))
            #load the source image representing a 'golden turbocharger', the talisman that is gained with each new completed course (acquire all six to unlock 4th car)
            turborender = pygame.transform.scale(pygame.image.load('images/objects/goldenturbo.png'), (54,50))
            #display the out-of-game menu frame
            DISPLAY.blit(gvar.WINDOW, (0,0))
            #if on the car select screen render the respective car's image to give off feel of shuffling through garage, along with the number of golden turbos, and the car name
            if gvar.FRAME == 2:
                DISPLAY.blit(carrender, (WIDTH/2-gvar.CARXSCALE/2,HEIGHT/2-gvar.CARYADJUST))
                #in the gamedata file the number of ones is the number of completed courses ('0000000'-no courses completed, '1111111'-all courses completed and special car unlocked)
                if gvar.GAMEDATA.count('1') < 6:
                    for i in range(gvar.GAMEDATA.count('1')):
                        DISPLAY.blit(turborender, ((WIDTH/2+12.5)-((3-i)*75),385))
                else:
                    for i in range(6):
                        DISPLAY.blit(turborender, ((WIDTH/2+12.5)-((3-i)*75),385))
                cartitlebox = cartitle.get_rect()
                cartitlebox.centerx = WIDTH/2
                cartitlebox.centery = HEIGHT/2-gvar.CARYADJUST-40
                DISPLAY.blit(cartitle, cartitlebox)
            #if on the course select screen render the title of the course about to be selected
            elif gvar.FRAME == 3:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            #if on the course complete screen render the title of the course completed
            elif gvar.FRAME == 4:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            #if on the course failed screen render the title of the course failed
            elif gvar.FRAME == 5:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            #if on the new car unlocked screen render the image of the new car
            elif gvar.FRAME == 6:
                carrender = pygame.transform.scale(pygame.image.load('images/player/side4.png'), (570,156))
                DISPLAY.blit(carrender, (100,HEIGHT/2-50))
                coursetitle = coursefont.render('x6', True, WHITE, BLACK)
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.left = 125
                coursetitlebox.centery = 450
                DISPLAY.blit(coursetitle, coursetitlebox)

            #user input
            keyreader.read()


        #things happening during the in-game scenario
        else:
            #display the course background
            DISPLAY.blit(gvar.WINDOW, (2*gvar.STREET.tilt-100,0))
            #create the textbox content and surfaces to display the player's speed, the cource's completion percentage and lap number, and the player's condition
            speedtext = ingamefontbig.render((str(round((gvar.STREET.speed/6.9)*25000)) + ' km/h'), True, WHITE, BLACK)
            completiontext = ingamefontsmall.render('[COMPLETION: ' + (str(round((gvar.STREET.distance/len(gvar.STREET.trackroad))*100)) + '% ] [LAP ' + str(gvar.STREET.lapnum) + '/3]'), True, WHITE, BLACK)
            conditiontext = ingamefontsmall.render('CONDITION: ' + (str(round(gvar.CONDITION)) + ' %'), True, WHITE, BLACK)
            speedbox = speedtext.get_rect()
            speedbox.top = 10
            speedbox.left = 10
            completionbox = completiontext.get_rect()
            completionbox.top = 10
            completionbox.right = WIDTH-10
            conditionbox = conditiontext.get_rect()
            conditionbox.top = 40
            conditionbox.right = WIDTH-10

            #update the lasers
            gvar.LASERS.update()
            #make the road read the track data
            gvar.STREET.readtrack()
            #update the road accordingly
            gvar.STREET.update()
            #move the player (the car) as defined by the user's input
            gvar.RACER.move()

            #put speed limits on the cars: 1-fast, 2-medium, 3-slow, 4-superfast (maxes out framerate)
            if gvar.CARNUM == 1:
                if gvar.STREET.speed > .08:
                    gvar.STREET.speed = .079
            if gvar.CARNUM == 2:
                if gvar.STREET.speed > .07:
                    gvar.STREET.speed = .069
            if gvar.CARNUM == 3:
                if gvar.STREET.speed > .06:
                    gvar.STREET.speed = .059

            #simulate centrifugal force (the faster the player is moving the more force applied on turns)
            if gvar.STREET.speed > 0:
                if gvar.STREET.tilt == 0:
                    gvar.RACER.dxs = 0
                elif gvar.STREET.tilt == -1:
                    gvar.RACER.dxs = 2.5*(gvar.STREET.speed+.001)
                elif gvar.STREET.tilt == 1:
                    gvar.RACER.dxs = -2.5*(gvar.STREET.speed+.001)
            else:
                gvar.RACER.dxs = 0

            #collision detection between the player object and the laserbeam object (if hit the condition goes down, which each ascending car being more durable)
            if ((gvar.LASERS.x1 >= gvar.RACER.x and gvar.LASERS.x1 <= gvar.RACER.x+gvar.RACER.width and gvar.LASERS.y1 >= -(gvar.LASERS.height-gvar.RACER.y))
                or (gvar.LASERS.x2 >= gvar.RACER.x and gvar.LASERS.x2 <= gvar.RACER.x+gvar.RACER.width and gvar.LASERS.y2 >= -(gvar.LASERS.height-gvar.RACER.y))
                or (gvar.LASERS.x3 >= gvar.RACER.x and gvar.LASERS.x3 <= gvar.RACER.x+gvar.RACER.width and gvar.LASERS.y3 >= -(gvar.LASERS.height-gvar.RACER.y))
                or (gvar.LASERS.x1+gvar.LASERS.width >= gvar.RACER.x and gvar.LASERS.x1+gvar.LASERS.width <= gvar.RACER.x+gvar.RACER.width and gvar.LASERS.y1 >= -(gvar.LASERS.height-gvar.RACER.y))
                or (gvar.LASERS.x2+gvar.LASERS.width >= gvar.RACER.x and gvar.LASERS.x2+gvar.LASERS.width <= gvar.RACER.x+gvar.RACER.width and gvar.LASERS.y2 >= -(gvar.LASERS.height-gvar.RACER.y))
                or (gvar.LASERS.x3+gvar.LASERS.width >= gvar.RACER.x and gvar.LASERS.x3+gvar.LASERS.width <= gvar.RACER.x+gvar.RACER.width and gvar.LASERS.y3 >= -(gvar.LASERS.height-gvar.RACER.y))):
                gvar.CONDITION -= .1/gvar.CARNUM

            #if the course is completed (100% completeion on final lap) then set ingame to false, switch music, save new game data, and change menu frame
            if (round((gvar.STREET.distance/len(gvar.STREET.trackroad))*100) >= 100 and gvar.STREET.lapnum >= 3):
                gvar.INGAME = False
                #play mission completed music
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/musicc.mp3')
                if gvar.PLAYMUSIC == True:
                    pygame.mixer.music.play(-1)
                gvar.GAMEDATA = gvar.GAMEDATA[:(gvar.COURSENUM-1)] + '1' + gvar.GAMEDATA[(gvar.COURSENUM):]
                file=open('data/gamedata/gamedata.txt','w+')
                file.write(gvar.GAMEDATA)
                file.close()
                #win frame
                gvar.FRAME = 4

            #if condition runs out then set ingame to false, switch music, save new game data, and change menu frame
            if (round(gvar.CONDITION) <= 0):
                gvar.INGAME = False
                #play mission failed music
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/musicf.mp3')
                if gvar.PLAYMUSIC == True:
                    pygame.mixer.music.play(-1)
                #lose frame
                gvar.FRAME = 5

            #user input
            keyreader.read()

            #display each object
            DISPLAY.blit(gvar.RACER.image, (gvar.RACER.x,gvar.RACER.y))
            DISPLAY.blit(gvar.LASERS.image, (gvar.LASERS.x1,gvar.LASERS.y1))
            DISPLAY.blit(gvar.LASERS.image, (gvar.LASERS.x2,gvar.LASERS.y2))
            DISPLAY.blit(gvar.LASERS.image, (gvar.LASERS.x3,gvar.LASERS.y3))
            DISPLAY.blit(speedtext, speedbox)
            DISPLAY.blit(completiontext, completionbox)
            DISPLAY.blit(conditiontext, conditionbox)

        #the following line continuously calls the while loop
        pygame.display.update()

#the following line calls the main function and starts the game
main()
