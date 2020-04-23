#import pygame, local class files, and other necessary libraries
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *
from player import Player
#from trackgenerator import TrackGenerator
from road import Road
from laserbeam import Laserbeam

#set default display dimensions and create a display to render the game, alongside some colors for text display
WIDTH = 800
HEIGHT = 500
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
DISPLAY.fill(BLACK)

def main():
    """
	The 'main()' function is used to run the game, manage which objects render, and play music,
    along with saving data and pulling data to be read by the objects that need it.

	First all the objects are initialized and then in the following while loop all of the interactions
	(from user input, to collision detection, to the head-up display and ui) are handled.
	"""
    #setup pygame window
    pygame.init()
    pygame.display.set_caption('PyRacer')
    #trackgen = TrackGenerator() <- if you want to create new tracks uncomment this...
    #trackgen.generate() <- ...and this
    #boolean to determine if the game is in driving mode and should render the player, road, and obstacles or not
    ingame = False
    #set default menu frame: 1-start, 2-car select, 3-course select, 4-win frame, 5-lose frame
    frame = 1
    #set default course to render as defined in road.py
    course = 1
    #set default car to render as defined in player.py
    car = 1
    #boolean to determine if the game is on the start screen
    startscreen = True
    #value to determine the condition of the user's car (if 0 then mission failed)
    condition = 100
    #define the different fonts that will be used
    carfont = pygame.font.Font('fonts/Retron2000.ttf', 32)
    coursefont = pygame.font.Font('fonts/Retron2000.ttf', 48)
    ingamefontbig = pygame.font.Font('fonts/Retron2000.ttf', 32)
    ingamefontsmall = pygame.font.Font('fonts/Retron2000.ttf', 16)
    #load the default music and play continuously
    pygame.mixer.music.load('music/music0.mp3')
    pygame.mixer.music.play(-1)
    #load game data file
    filename = 'data/gamedata/gamedata.txt'
    with open(filename) as file:
        gamedata = file.readline()
    file.close()

    while True:
        """
		As mentioned before this loop handeles all of the interactions.

		Although dispersed, this while loop can be split into three overall concepts:
		Graphics Rendering, User Input, and Collision Detection.

        Two of the three concepts are presented in the 'ingame == False' statement while
        all three are presented in the 'ingame == True' statement.
		"""
        #things happening in the out-of-game scenario
        if ingame == False:
            #graphics rendering
            #if the menu frame is past the first one, we are no longer on the start screen (this is used to prevent a bug when going back to the start screen)
            if frame > 1:
                startscreen = False
            #depending on the current car value the image scaling, y-axis adujust for centering, and listed name will change
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
            #depending on the current course value the listed name will change
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
            #load the source image representing the out-of-game frame the menu is on
            window = pygame.transform.scale(pygame.image.load('images/menuframes/frame' + str(frame) + '.png'), (800,500))
            #create pygame surface to render car name text (black background with white text)
            cartitle = carfont.render(carname, True, WHITE, BLACK)
            #create pygame surface to render course name text (black background with white text)
            coursetitle = coursefont.render(coursename, True, WHITE, BLACK)
            #load the source image representing the car in the car select screen
            carrender = pygame.transform.scale(pygame.image.load('images/player/front' + str(car) + '.png'), (carxscale,caryscale))
            #load the source image representing a 'golden turbocharger', the talisman that is gained with each new completed course (acquire all six to unlock 4th car)
            turborender = pygame.transform.scale(pygame.image.load('images/objects/goldenturbo.png'), (54,50))
            #display the out-of-game menu frame
            DISPLAY.blit(window, (0,0))
            #if on the car select screen render the respective car's image to give off feel of shuffling through garage, along with the number of golden turbos, and the car name
            if frame == 2:
                DISPLAY.blit(carrender, (WIDTH/2-carxscale/2,HEIGHT/2-caryadjust))
                #in the gamedata file the number of ones is the number of completed courses ('000000'-no courses completed, '111111'-all courses completed)
                for i in range(gamedata.count('1')):
                    DISPLAY.blit(turborender, ((WIDTH/2+12.5)-((3-i)*75),385))
                cartitlebox = cartitle.get_rect()
                cartitlebox.centerx = WIDTH/2
                cartitlebox.centery = HEIGHT/2-caryadjust-40
                DISPLAY.blit(cartitle, cartitlebox)
            #if on the course select screen render the title of the course about to be selected
            elif frame == 3:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            #if on the course complete screen render the title of the course completed
            elif frame == 4:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)
            #if on the course failed screen render the title of the course failed
            elif frame == 5:
                coursetitlebox = coursetitle.get_rect()
                coursetitlebox.centerx = WIDTH/2
                coursetitlebox.centery = HEIGHT/2
                DISPLAY.blit(coursetitle, coursetitlebox)

            #user input
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #if any key is pressed on the start screen proceed to the car select screen
                    if frame == 1 and startscreen == True:
                        if event.key != (pygame.K_LSHIFT or pygame.K_RSHIFT):
                            frame = 2
                    #move left to change which car/course that will be selected
                    if event.key == pygame.K_LEFT:
                        if frame == 2:
                            if car > 1:
                                car -= 1
                        elif frame == 3:
                            if course > 1:
                                course -= 1
                    #move right to change which car/course that will be selected (within the bounds of what has been unlocked)
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
                    #press enter to make your selection
                    if event.key == pygame.K_RETURN and startscreen == False:
                        #select car
                        if frame == 2:
                            frame = 3
                        #load the appropriate course background, create the game objects, reset car condition, start the mucis, and well, start the game!
                        elif frame == 3:
                            window = pygame.transform.scale(pygame.image.load('images/backgrounds/bg' + str(course) + '.png'), (1000,302))
                            street = Road(course)
                            racer = Player(car, carxscale/2,caryscale/2, WIDTH/2, (7*HEIGHT/8-20-caryadjust/2))
                            lasers = Laserbeam(course)
                            condition = 100
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/music' + str(course) + '.mp3')
                            pygame.mixer.music.play(-1)
                            ingame = True
                        #go back to car select frame and reset music to default
                        elif frame == 4 or frame == 5:
                            frame = 2
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('music/music0.mp3')
                            pygame.mixer.music.play(-1)
                    #go back to the previous menu frame
                    if event.key == (pygame.K_LSHIFT or pygame.K_RSHIFT):
                        if frame == 2:
                            frame = 1
                            startscreen = True
                        elif frame == 3:
                            frame = 2
                    #reset game data
                    if event.key == (pygame.K_r):
                        file=open('data/gamedata/gamedata.txt','w+')
                        gamedata = '000000'
                        file.write(gamedata)
                        file.close()

        #things happening in the in-game scenario
        else:
            #display the course background
            DISPLAY.blit(window, (2*street.tilt-100,0))
            #create the textbox content and surfaces to display the player's speed, the cource's completion percentage and lap number, and the player's condition
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

            #update the lasers
            lasers.update()
            #make the road read the track data
            street.readtrack()
            #update the road accordingly
            street.update()
            #move the player (the car) as defined by the user's input
            racer.move()

            #put speed limits on the cars: 1-fast, 2-medium, 3-slow, 4-superfast (maxes out framerate)
            if car == 1:
                if street.speed > .08:
                    street.speed = .079
            if car == 2:
                if street.speed > .07:
                    street.speed = .069
            if car == 3:
                if street.speed > .06:
                    street.speed = .059

            #simulate centrifugal force (the faster the player is moving the more force applied on turns)
            if street.speed > 0:
                if street.tilt == 0:
                    racer.dxs = 0
                elif street.tilt == -1:
                    racer.dxs = 2.5*(street.speed+.001)
                elif street.tilt == 1:
                    racer.dxs = -2.5*(street.speed+.001)
            else:
                racer.dxs = 0

            #collision detection between the player object and the laserbeam object (if hit the condition goes down, which each ascending car being more durable)
            if ((lasers.x1 >= racer.x and lasers.x1 <= racer.x+racer.width and lasers.y1 >= -(lasers.height-racer.y))
                or (lasers.x2 >= racer.x and lasers.x2 <= racer.x+racer.width and lasers.y2 >= -(lasers.height-racer.y))
                or (lasers.x3 >= racer.x and lasers.x3 <= racer.x+racer.width and lasers.y3 >= -(lasers.height-racer.y))
                or (lasers.x1+lasers.width >= racer.x and lasers.x1+lasers.width <= racer.x+racer.width and lasers.y1 >= -(lasers.height-racer.y))
                or (lasers.x2+lasers.width >= racer.x and lasers.x2+lasers.width <= racer.x+racer.width and lasers.y2 >= -(lasers.height-racer.y))
                or (lasers.x3+lasers.width >= racer.x and lasers.x3+lasers.width <= racer.x+racer.width and lasers.y3 >= -(lasers.height-racer.y))):
                condition -= .1/car

            #if the course is completed (100% completeion on final lap) then set ingame to false, switch music, save new game data, and change menu frame
            if (round((street.distance/len(street.trackroad))*100) >= 100 and street.lapnum >= 3):
                ingame = False
                #play mission completed music
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/musicc.mp3')
                pygame.mixer.music.play(-1)
                gamedata = gamedata[:(course-1)] + '1' + gamedata[(course):]
                file=open('data/gamedata/gamedata.txt','w+')
                file.write(gamedata)
                file.close()
                #win frame
                frame = 4

            #if condition runs out then set ingame to false, switch music, save new game data, and change menu frame
            if (round(condition) <= 0):
                ingame = False
                #play mission failed music
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/musicf.mp3')
                pygame.mixer.music.play(-1)
                #lose frame
                frame = 5

            #user input
            for gameevent in pygame.event.get():
                if gameevent.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if gameevent.type == pygame.KEYDOWN:
                    #player moves left when the left key is pressed and turning left image is set
                    if gameevent.key == pygame.K_LEFT:
                        if car > 4:
                            racer.dx = -10*(.001+street.speed)/car
                        else:
                            racer.dx = -10*(.001+street.speed)/.75
                        racer.image = racer.imgleft
                    #player moves right when the right key is pressed and turning right image is set
                    if gameevent.key == pygame.K_RIGHT:
                        if car > 4:
                            racer.dx = 10*(.001+street.speed)/car
                        else:
                            racer.dx = 10*(.001+street.speed)/.75
                        racer.image = racer.imgright
                    #player accelerates (the road progresses forward at a continuously increasing rate until max speed) when the up key is pressed
                    if gameevent.key == pygame.K_UP:
                        if car != 4:
                            street.sp = .0003/car
                        elif car == 4:
                            street.sp = .0004
                    #player decelerates (the road progresses forward at a continuously decreasing rate until zero) when the down key is pressed
                    if gameevent.key == pygame.K_DOWN:
                        street.sp = -.00035/car

                if gameevent.type == pygame.KEYUP:
                    #player stops moving left
                    if gameevent.key == pygame.K_LEFT:
                        racer.dx = 0
                        racer.image = racer.img
                    #player stops moving right
                    if gameevent.key == pygame.K_RIGHT:
                        racer.dx = 0
                        racer.image = racer.img
                    #player stops accelerating
                    if gameevent.key == pygame.K_UP:
                        street.sp = -.0001
                    #player stops decelerating as quickly
                    if gameevent.key == pygame.K_DOWN:
                        street.sp = -.0001

            #display each object
            DISPLAY.blit(racer.image, (racer.x,racer.y))
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
