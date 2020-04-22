#import pygame
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *

#set default display dimensions
WIDTH = 800
HEIGHT = 500

class Player:
	"""
	This 'Player' class is used to display and update the player object (the car that the user controls).
	"""
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
		"""
		The '__init__()' function defines the source images for each car as well as some positioning and collision defaults.
		"""
		#car's image and hitbox width
		self.width = width
		#car's image and hitbox height
		self.height = height
		#car's x position
		self.x = x
		#car's y position
		self.y = y
		#car's change in x (if moving)
		self.dx = 0
		#the selected car will use the source images correlating to its numeral value
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
		#the simulated centrefugal force
		self.dxs = 0
	def move(self):
		"""
		The 'move()' makes the car move sideways.
		"""
		#change x by dx and dxs
		self.x += self.dx + self.dxs
		#check to make sure that thw car is within the bounds of the display
		if self.x >= (WIDTH-self.width):
			self.x = WIDTH-self.width
		if self.x <= 0:
			self.x = 0
