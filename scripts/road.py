import pygame, sys
from pygame.locals import *
import numpy as np
from trackgenerator import TrackGenerator
import time

WIDTH = 800
HEIGHT = 500
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)


class Road:
	def __init__(self, track = 1, x = 0, y = 0):
		#track 1 = speedway, track 2 = countryside, track 3 = tundra, track 4 = desert, track 5 = city, track 6 = outerspace
		self.starttime = time.clock()
		self.currenttime = time.clock()
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
		self.roadwidth = 1000
		self.sidewidth = 1000
		self.road = np.zeros(200, dtype=object)
		self.ground = np.zeros(100, dtype=object)
		self.sidelines = np.zeros(100, dtype=object)
		self.tilt = 0
		self.distance = 0
		self.accelerate = False
		self.speed = 0
		self.sp = 0
		self.linecolor = 0
		self.lapnum = 1
		self.startrace = True
		filename = 'tracks/track' + str(track) + '.txt'
		with open(filename) as file:
			self.trackroad = file.readline()
		file.close()

	def update(self):
		for roadslice in range(100):
			if self.linecolor % 2 != 0:
				self.ground[roadslice] = pygame.draw.rect(DISPLAY, self.GROUND1, (-100, HEIGHT-2*(roadslice), 1000, 2))
			if self.linecolor % 2 == 0:
				self.ground[roadslice] = pygame.draw.rect(DISPLAY, self.GROUND2, (-100, HEIGHT-2*(roadslice), 1000, 2))
			roadslice+=1
			self.linecolor += 1
		roadslice = 0
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
		for roadslice in range(200):
			self.road[roadslice] = pygame.draw.rect(DISPLAY, self.ROAD, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((roadslice*roadslice)/5000))), HEIGHT-(roadslice), int(self.roadwidth), 1))
			self.roadwidth-=5
			roadslice+=1
		self.roadwidth=1000

	def readtrack(self):
		self.currenttime = time.clock()-self.starttime
		if (self.currenttime-self.starttime) > (.09-self.speed) or self.startrace == True:
			if self.distance >= len(self.trackroad):
				self.distance = 0
				self.lapnum += 1
			self.speed += self.sp
			if self.speed <= 0:
				self.speed = 0
			elif self.speed >= .08:
				self.speed = .079
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
			self.startrace = False	
			self.starttime = self.currenttime
