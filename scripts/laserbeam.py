import pygame, sys
from pygame.locals import *
import numpy as np
import time
import random

WIDTH = 800
HEIGHT = 500
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

class Laserbeam:
	def __init__(self, track = 1, img = pygame.transform.scale(pygame.image.load('images/objects/laserbeam.png'), (80, 500))):
		self.starttime = time.clock()
		self.currenttime = time.clock()
		self.width = 80
		self.height = 500
		self.fallrate = 2
		self.image = img
		self.lasercombo = 2
		self.touchdown = True
		self.x1 = WIDTH/4-(self.width/2)
		self.x2 = 2*WIDTH/4-(self.width/2)
		self.x3 = 3*WIDTH/4-(self.width/2)
		self.y1 = -self.height
		self.y2 = -self.height
		self.y3 = -self.height
		if track == 1 or track == 2:
			self.mincombos = 1
			self.maxcombos = 3
		elif track == 3 or track == 4:
			self.mincombos = 1
			self.maxcombos = 6
		elif track == 5 or track == 6:
			self.mincombos = 4
			self.maxcombos = 6
	def update(self):
		self.currenttime = time.clock()-self.starttime
		if (self.currenttime-self.starttime) > (.01-(self.fallrate/1000)):
			if self.touchdown == True:
				self.lasercombo = random.randint(self.mincombos, self.maxcombos)
				self.y1 = -self.height
				self.y2 = -self.height
				self.y3 = -self.height
				self.fallrate *= 1.01
				self.touchdown = False
			else:
				if (self.y1 >= -50) or (self.y2 >= -50) or (self.y3 >= -50):
					self.touchdown = True
				if self.lasercombo == 1:
					self.y1 += self.fallrate
					self.y2 += 0
					self.y3 += 0
				elif self.lasercombo == 2:
					self.y1 += 0
					self.y2 += self.fallrate
					self.y3 += 0
				elif self.lasercombo == 3:
					self.y1 += 0
					self.y2 += 0
					self.y3 += self.fallrate
				elif self.lasercombo == 4:
					self.y1 += self.fallrate
					self.y2 += self.fallrate
					self.y3 += 0
				elif self.lasercombo == 5:
					self.y1 += self.fallrate
					self.y2 += 0
					self.y3 += self.fallrate
				elif self.lasercombo == 6:
					self.y1 += 0
					self.y2 += self.fallrate
					self.y3 += self.fallrate
			self.starttime = self.currenttime
