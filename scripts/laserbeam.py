#import pygame and other necessary libraries
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *
import time
import random

#set default display dimensions
WIDTH = 800
HEIGHT = 500

class Laserbeam:
	"""
	This 'Laserbeam' class is used to display and update the laserbeam object (the obstacles that the user must avoid).
	"""
	def __init__(self, track = 1, img = pygame.transform.scale(pygame.image.load('images/objects/laserbeam.png'), (85, 500))):
		"""
		The '__init__()' function defines the source image for the lasers and the possibilities of how the
        lasers will act, as well as some positioning and collision defaults.
		"""
		#this sets the initial time to determine when to update the lasers
		self.starttime = time.clock()
		#this sets the given time to compare against the initial time
		self.currenttime = time.clock()
		#each laser's width
		self.width = 85
		#each laser's height
		self.height = 500
		#this is the constant at which the lasers will fall
		self.fallrate = 2
		#image to be displayed while running
		self.image = img
		#this integer corresponds to how the lasers will render: 1-left only, 2-middle only, 3-right only, 4-left and middle, 5-left and right, 6-middle and right
		self.lasercombo = 0
		#this boolean checks to see if a laser has hit the groud, if so all the lasers reset
		self.touchdown = True
		#defining each laser's x position
		self.x1 = WIDTH/4-(self.width/2)-45
		self.x2 = 2*WIDTH/4-(self.width/2)
		self.x3 = 3*WIDTH/4-(self.width/2)+45
		#defining each laser's y position
		self.y1 = -self.height
		self.y2 = -self.height
		self.y3 = -self.height
		#depending on the chosen track the possible combinations will differ with graduating difficulty
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
		"""
		The 'update()' function defines how the lasers will act depending on a random given number, and controls the speeds at which they move.
		"""
		#update the current time
		self.currenttime = time.clock()
		#if the differences in the times surpasses the framerate threshold the lasers will update accordingly
		if (self.currenttime-self.starttime) > (.01-(self.fallrate/1000)):
			#if self.touchdown is true the lasers will reset and will move faster next time
			if self.touchdown == True:
				self.lasercombo = random.randint(self.mincombos, self.maxcombos)
				self.y1 = -self.height
				self.y2 = -self.height
				self.y3 = -self.height
				self.fallrate *= 1.005
				self.touchdown = False
			#if self.touchdown is false the lasers will descend accordingly
			else:
				if (self.y1 >= -20) or (self.y2 >= -20) or (self.y3 >= -20):
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
			#update the start time to continue the chain
			self.starttime = time.clock()
