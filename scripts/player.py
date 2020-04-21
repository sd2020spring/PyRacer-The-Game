import pygame, sys
from pygame.locals import *

class Player:
	def __init__(self, car = 1, width = 0, height = 0, x = 0, y = 0,
				img1 = pygame.transform.scale(pygame.image.load('images/player/straight1.png'), (116, 64)),
				imgleft1 = pygame.transform.scale(pygame.image.load('images/player/left1.png'), (116, 64)),
				imgright1 = pygame.transform.scale(pygame.image.load('images/player/right1.png'), (116, 64)),
				img2 = pygame.transform.scale(pygame.image.load('images/player/straight2.png'), (116, 85)),
				imgleft2 = pygame.transform.scale(pygame.image.load('images/player/left2.png'), (116, 85)),
				imgright2 = pygame.transform.scale(pygame.image.load('images/player/right2.png'), (116, 85)),
				img3 = pygame.transform.scale(pygame.image.load('images/player/straight3.png'), (128, 116)),
				imgleft3 = pygame.transform.scale(pygame.image.load('images/player/left3.png'), (128, 116)),
				imgright3 = pygame.transform.scale(pygame.image.load('images/player/right3.png'), (128, 116)),
				img4 = pygame.transform.scale(pygame.image.load('images/player/straight4.png'), (122, 64)),
				imgleft4 = pygame.transform.scale(pygame.image.load('images/player/left4.png'), (122, 64)),
				imgright4 = pygame.transform.scale(pygame.image.load('images/player/right4.png'), (122, 64)), dxs = 0):
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
		#original reference image (to prevent quality loss from transformations)
		if car == 1:
			self.img = img1
			self.imgleft = imgleft1
			self.imgright = imgright1
		elif car == 2:
			self.img = img2
			self.imgleft = imgleft2
			self.imgright = imgright2
		elif car == 3:
			self.img = img3
			self.imgleft = imgleft3
			self.imgright = imgright3
		elif car == 4:
			self.img = img4
			self.imgleft = imgleft4
			self.imgright = imgright4
		#image to be displayed while running
		self.image = pygame.transform.rotate(self.img, 0)
		#xadjust and yadjust are constants to make the x and y coordinates in the self.hitbox correspond with the center of the image
		self.xadjust = -width/2
		self.yadjust = -height/2
		#hitbox- simplifies boundaries for collision or eating detection
		self.hitbox = (self.x+self.xadjust, self.y+self.yadjust, self.width, self.height)
		#number of bugs the self has eaten
		self.dxs = 0
	def move(self):
		#change x by dx
		self.x += self.dx + self.dxs
		#change y by dy
		self.y += self.dy
		#moves the hitbox so that it always corresponds to the position
		self.hitbox = (self.x+self.xadjust, self.y+self.yadjust, self.width, self.height)
	def gameover(self):
		#stops along x axis
		self.dx = 0
		#stops along y axis
		self.dy = 0
