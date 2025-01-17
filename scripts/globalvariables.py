#import pygame and other necessary libraries
from pathlib import Path
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *

class GlobalVariables():
    """
    The `GlobalVariables` handles the all the global variables in the game.
    """
    def __init__(self):
        """
		The `__init__()` function initializes every single global variable that all the other objects can access during runtime.
		"""
        self.WIDTH = 800
        self.HEIGHT = 500
        self.DISPLAY = pygame.display.set_mode((self.WIDTH,self.HEIGHT),0,32)
        #boolean to determine if the game is in driving mode and should render the player, road, and obstacles or not
        self.INGAME = False
        #set default menu frame: 1-start, 2-car select, 3-course select, 4-win frame, 5-lose frame
        self.FRAME = 1
        #set default course to render as defined in road.py
        self.COURSENUM = 1
        #set default car to render as defined in player.py
        self.CARNUM = 1
        #boolean to determine if the game is on the start screen
        self.STARTSCREEN = True
        #value to determine the condition of the user's car (if 0 then mission failed)
        self.CONDITION = 100
        #boolean to toggle music on or off
        self.PLAYMUSIC = True
        #load game data file
        datafile = Path('data/gamedata/gamedata.txt')
        with open(datafile) as file:
            self.GAMEDATA = file.readline()
        file.close()
        #boolean to toggle music on or off
        playmusic = True
        #render background image
        menufilepath = Path('images/menuframes/frame1')
        menufile = str(menufilepath)+'.png'
        self.WINDOW = pygame.transform.scale(pygame.image.load(menufile), (self.WIDTH,self.HEIGHT))
        #initialize dummy car scalings and vertical adjustments
        self.CARXSCALE = 0
        self.CARYSCALE = 0
        self.CARYADJUST = 0
        #initialize dummy road object
        self.STREET = None
        #initialize dummy player object
        self.RACER = None
        #initialize dummy laser object
        self.LASERS = None
        self.RACERDX = 1
        self.STREETSPEED = 0
        self.STREETSP = 0

#define the global object with all the varibles defined inside
global gvar
gvar = GlobalVariables()
