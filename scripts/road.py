#import pygame and other necessary libraries
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *
from globalvariables import GlobalVariables, gvar
import numpy as np
import time

#initialize the source for global variables from import
global gvar
#set default display dimensions and create a display to render the road
WIDTH = gvar.WIDTH
HEIGHT = gvar.HEIGHT
DISPLAY = gvar.DISPLAY

class Road:
    """
    This 'Road' class is used to display and update the road object (the simulation of forward movement in the game).
    """
    def __init__(self, track = 1, x = 0, y = 0):
        """
        The '__init__()' function defines the aesthetics of each road that can be rendered and pulls the appropriate track data to read from.
        """
        #this sets the initial time to determine when to update the lasers
        self.starttime = time.clock()
        #this sets the given time to compare against the initial time
        self.currenttime = time.clock()
        #these if statments determine the color scheme for each course: 1-speedway, 2-countryside, 3-tundra, 4-desert, 5-city, 6-space
        if track == 1:
            self.ROAD = (50,50,50)
            self.GROUND1 = (150,225,50)
            self.GROUND2 = (100,205,20)
            self.SIDES1 = (255,0,0)
            self.SIDES2 = (255,255,255)
        elif track == 2:
            self.ROAD = (205,205,120)
            self.GROUND1 = (80,150,0)
            self.GROUND2 = (60,120,0)
            self.SIDES1 = (238,224,0)
            self.SIDES2 = (187,176,0)
        elif track == 3:
            self.ROAD = (200,200,200)
            self.GROUND1 = (200,220,220)
            self.GROUND2 = (180,200,200)
            self.SIDES1 = (250,250,255)
            self.SIDES2 = (240,240,240)
        elif track == 4:
            self.ROAD = (200,200,150)
            self.GROUND1 = (225,225,160)
            self.GROUND2 = (205,205,120)
            self.SIDES1 = (160,160,120)
            self.SIDES2 = (150,150,100)
        elif track == 5:
            self.ROAD = (25,25,25)
            self.GROUND1 = (5,5,5)
            self.GROUND2 = (0,0,0)
            self.SIDES1 = (100,100,100)
            self.SIDES2 = (50,50,50)
        elif track == 6:
            self.ROAD = (5,5,5)
            self.GROUND1 = (0,0,0)
            self.GROUND2 = (0,0,0)
            self.SIDES1 = (255,255,50)
            self.SIDES2 = (0,0,0)
        #default width of each slice that makes the road
        self.roadwidth = 1000
        #default width of each slice that makes the sidelines
        self.sidewidth = 1000
        #create a default list of 200 objects that will be comprised of each slice of the road
        self.road = np.zeros(200, dtype=object)
        #create a default list of 100 objects that will be comprised of each slice of the ground
        self.ground = np.zeros(100, dtype=object)
        #create a default list of 100 objects that will be comprised of each slice of the sidelines
        self.sidelines = np.zeros(100, dtype=object)
        #the individual road/sideline slice x-axis offset from the center
        self.tilt = 0
        #the current index in the list of the track data
        self.distance = 0
        #the framerate update constant
        self.speed = 0
        #the rate of change of the framerate update constant
        self.sp = 0
        #this variable determines whether the current road/ground/sideline slice will be the first of second allocated color
        self.linecolor = 0
        #the number of complete progessions through the track data that the road has read
        self.lapnum = 1
        #open the given track's data file
        filename = 'data/tracks/track' + str(track) + '.txt'
        with open(filename) as file:
            self.trackroad = file.readline()
        file.close()

    def update(self):
        """
        The 'update()' function defines how each slice of the road/ground/sidelines will render
        depending on self.tilt, and the index of the respective list.
        """
        #create 100 slices of the ground that alternate colors on each frame switch
        for roadslice in range(100):
            if self.linecolor % 2 != 0:
                self.ground[roadslice] = pygame.draw.rect(DISPLAY, self.GROUND1, (-100, HEIGHT-2*(roadslice), 1000, 2))
            if self.linecolor % 2 == 0:
                self.ground[roadslice] = pygame.draw.rect(DISPLAY, self.GROUND2, (-100, HEIGHT-2*(roadslice), 1000, 2))
            roadslice+=1
            self.linecolor += 1
        roadslice = 0
        #create 100 slices of the sidelines that alternate colors on each frame switch, narrow with descending height values, and move accordingly with the tilt
        for roadslice in range(100):
            if self.linecolor % 2 != 0:
                self.road[roadslice] = pygame.draw.rect(DISPLAY, self.SIDES1, (((WIDTH/2)-(self.sidewidth/2) + (2*self.tilt*((2*roadslice*roadslice)/5000))), HEIGHT-2*(roadslice), int(self.sidewidth), 2))
            if self.linecolor % 2 == 0:
                self.road[roadslice] = pygame.draw.rect(DISPLAY, self.SIDES2, (((WIDTH/2)-(self.sidewidth/2) + (2*self.tilt*((2*roadslice*roadslice)/5000))), HEIGHT-2*(roadslice), int(self.sidewidth), 2))
            self.sidewidth-=12
            roadslice+=1
            self.linecolor += 1
        self.sidewidth = 1200
        roadslice = 0
        #create 200 slices of the road that narrow with descending height values and move accordingly with the tilt with each frame switch
        for roadslice in range(200):
            self.road[roadslice] = pygame.draw.rect(DISPLAY, self.ROAD, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((roadslice*roadslice)/5000))), HEIGHT-(roadslice), int(self.roadwidth), 1))
            self.roadwidth-=5
            roadslice+=1
        self.roadwidth=1000

    def readtrack(self):
        """
        The 'readtrack()' function reads through the track data file and dictates how the overall course will react on each frame switch.
        """
        #update the current time
        self.currenttime = time.clock()
        #if the differences in the times surpasses the framerate threshold the road/ground/sidelines slices will update accordingly
        if (self.currenttime-self.starttime) > (.12-self.speed):
            if self.distance >= len(self.trackroad):
                self.distance = 0
                self.lapnum += 1
            self.speed += self.sp
            #check to make sure the framerate is not too fast or slow
            if self.speed <= 0:
                self.speed = 0
            elif self.speed >= .09:
                self.speed = .089
            #if the framerate is withing the valid bounds give the appropriate values to update all the road/ground/sidelines slices by based on the track data
            elif self.speed > 0:
                if self.trackroad[self.distance] == '3':
                    self.tilt += 0
                    self.linecolor += 1
                    self.update()
                if self.trackroad[self.distance] == '2':
                    self.tilt -= 1
                    self.linecolor += 1
                    self.update()
                if self.trackroad[self.distance] == '4':
                    self.tilt += 1
                    self.linecolor += 1
                    self.update()
                if self.trackroad[self.distance] == '1':
                    self.tilt -= 0
                    self.linecolor += 1
                    self.update()
                if self.trackroad[self.distance] == '5':
                    self.tilt += 0
                    self.linecolor += 1
                    self.update()
                if self.distance < len(self.trackroad):
                    self.distance += 1
            #update the start time to continue the chain
            self.starttime = time.clock()
