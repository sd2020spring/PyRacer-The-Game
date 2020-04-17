import pygame, sys
from pygame.locals import *
import numpy as np
from trackgenerator import TrackGenerator
import time

WIDTH = 800
HEIGHT = 500
DGRAY = (25,50,25)
LGRAY = (50,100,50)
BEIGE = (225,225,160)
DBEIGE = (205,205,120)
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)


class Sidelines:
	def __init__(self, track = 0, width = 1100, height = 3, x = 0, y = 0, img = pygame.transform.scale(pygame.image.load('images/objects/tree.png'), (100, 100))):
		self.roadwidth = width
		self.roadheight = height
		self.road = np.zeros(50, dtype=object)
		self.ground = np.zeros(100, dtype=object)
		self.tilt = 0
		self.distance = 0
		self.accelerate = False
		self.speed = 0
		self.sp = 0
		self.linecolor = 0
		self.img = img
		self.image = pygame.transform.scale(self.img, (10,10))
		filename = 'tracks/track' + str(track) + '.txt'
		with open(filename) as file:
			self.trackroad = file.readline()
			self.tracksidelines = file.readline()
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
		for roadslice in range(50):
			if self.linecolor % 2 != 0:
				width = (2*(50-roadslice))
				height = (2*(50-roadslice))
				self.road[roadslice] = pygame.draw.rect(DISPLAY, DGRAY, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((16*roadslice*roadslice)/5000))), HEIGHT-4*(roadslice), int(self.roadwidth), int(self.roadheight)))
				DISPLAY.blit(self.image, (((WIDTH/2)-(self.roadwidth/2) - 4*width + (self.tilt*((16*roadslice*roadslice)/5000))),HEIGHT-4*(roadslice)))
				DISPLAY.blit(self.image, (((WIDTH/2)+(self.roadwidth/2) + 2*width + (self.tilt*((16*roadslice*roadslice)/5000))),HEIGHT-4*(roadslice)))
				self.image = pygame.transform.scale(self.img, (width, height))
			if self.linecolor % 2 == 0:
				self.road[roadslice] = pygame.draw.rect(DISPLAY, LGRAY, (((WIDTH/2)-(self.roadwidth/2) + (self.tilt*((16*roadslice*roadslice)/5000))), HEIGHT-4*(roadslice), int(self.roadwidth), int(self.roadheight)))
			self.roadwidth-=22
			roadslice+=1
			self.linecolor += 1
		self.roadwidth=1100

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
