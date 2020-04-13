import pygame, sys
from pygame.locals import *
import numpy as np
from trackgenerator import TrackGenerator
import time
import string

WIDTH = 800
HEIGHT = 500
DGRAY = (25,25,25)
LGRAY = (50,50,50)
BEIGE = (225,225,160)
DBEIGE = (205,205,120)
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)


class Road:
	def __init__(self, track = 0, width = 1000, height = 1, x = 0, y = 0):
		self.roadwidth = width
		self.roadheight = height
		self.road = np.zeros(200, dtype=object)
		self.ground = np.zeros(100, dtype=object)
		self.tilt = 0
		self.distance = 0
		self.accelerate = False
		self.reverse = False
		self.speed = 0
		self.sp = 0
		self.linecolor = 0
		self.objectset = 0
		filename = 'tracks/track' + str(track) + '.txt'
		with open(filename) as file:
			self.trackroad = file.readline()
			self.tracksidelines = file.readline()
			self.trackstreetobjects = file.readline()
		file.close()

	def update(self):
		for roadslice in range(100):
			if self.linecolor % 2 != 0:
				self.ground[roadslice] = pygame.draw.rect(DISPLAY, BEIGE, (-100, HEIGHT-2*(roadslice), 1000, 3))
			if self.linecolor % 2 == 0:
				self.ground[roadslice] = pygame.draw.rect(DISPLAY, DBEIGE, (-100, HEIGHT-2*(roadslice), 1000, 3))
			roadslice+=1
			self.linecolor += 1
		roadslice = 0
		for roadslice in range(200):
			if self.linecolor % 2 != 0:
				self.road[roadslice] = pygame.draw.rect(DISPLAY, DGRAY, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((roadslice*roadslice)/5000))), HEIGHT-(roadslice), int(self.roadwidth), int(self.roadheight)))
			if self.linecolor % 2 == 0:
				self.road[roadslice] = pygame.draw.rect(DISPLAY, LGRAY, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((roadslice*roadslice)/5000))), HEIGHT-(roadslice), int(self.roadwidth), int(self.roadheight)))
			self.roadwidth-=5
			roadslice+=1
			self.linecolor += 1
		self.roadwidth=1000

	def readtrack(self):
		if self.distance >= len(self.trackroad):
			self.distance = 0
			print('lap')
		self.speed += self.sp
		if self.speed <= 0:
			self.speed = 0
		elif self.speed >= .07:
			self.speed = .07

		time.sleep(.1 - self.speed)
		if self.speed > 0:
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
				if self.distance % 5 == 0:
					self.objectset += 1
