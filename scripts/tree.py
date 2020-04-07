import pygame, sys
from pygame.locals import *
from road import Road

WIDTH = 800
HEIGHT = 500
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

class Tree:
	def __init__(self, side = 0, width = 0, height = 0, x = WIDTH/2, y = HEIGHT/2, img = pygame.transform.scale(pygame.image.load('images/objects/tree.png'), (90, 120))):
		#side the object appears on
		self.side = side
		#hitbox width
		self.width = width
		#hitbox height
		self.height = height
		#x position
		self.x = x
		#y position
		self.y = y
		#change in x (if moving)
		self.dx = 0
		#change in y (if moving)
		self.dy = 0
		self.scaleby = 1
		#original reference image (to prevent quality loss from transformations)
		self.img = img
		#image to be displayed while running
		self.image = pygame.transform.scale(self.img, (9,12))
		#xadjust and yadjust are constants to make the x and y coordinates in the self.hitbox correspond with the center of the image
		self.dscaleby = 0
	def update(self):
		#change x by dscaleby
		if self.side == 0:
			self.x -= 4*self.dscaleby + self.dx
		else:
			self.x += 4*self.dscaleby + self.dx
		#change y by dscaleby
		self.y += 6*self.dscaleby
		self.scaleby += self.dscaleby
		DISPLAY.blit(self.image, (self.x,self.y))
		self.width = int(9*self.scaleby)
		self.height = int(12*self.scaleby)
		self.image = pygame.transform.scale(self.img, (self.width,self.height))

	def gameover(self):
		#stops along x axis
		self.dx = 0
		#stops along y axis
		self.dy = 0
