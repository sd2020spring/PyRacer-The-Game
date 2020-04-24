#import pygame and other necessary libraries
import contextlib
with contextlib.redirect_stdout(None):
    import pygame, sys
    from pygame.locals import *

class TrackGenerator:
	"""
	The 'TrackGenerator' class is used to generate a list of numbers that will correlate to how the in-game road will operate.

	Each number from 1 through 5 will cause the road to act differently:
	1 - Road holds to the left.
	2 - Road turns to the left.
	3 - Road holds to the center.
	4 - Road turns to the right.
	5 - Road holds to the right.
	"""
	def __init__(self):
		"""
		The '__init__()' function defines the possible pieces of the track that can be put together.
		"""
		#road stays straight
		self.straight = '3'
		#road turns left, holds left, then turns back right to the center
		self.left = '222222222222222222222222222222221111111111111111111111111111111144444444444444444444444444444444'
		self.left2 = '222222222222222211111111111111114444444444444444'
		self.left3 = '222222221111111144444444'
		#road turns right, holds right, then turns back left to the center
		self.right = '444444444444444444444444444444445555555555555555555555555555555522222222222222222222222222222222'
		self.right2 = '444444444444444455555555555555552222222222222222'
		self.right3 = '444444445555555522222222'
		#this string will be used to add and then save the generated data to a text file to pull from later
		self.road = ''

	def generate(self):
		"""
		The 'generate()' function uses the predefined pieces for a track written with strings to make a complete track.
		"""
		#continuously add pieces to the overall track
		'''
		#TRACK1
		for trackpieces in range(50):
			self.road += self.straight
		self.road += self.right
		self.road += self.right
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.left
		for trackpieces in range(25):
			self.road += self.straight
		self.road += self.left
		for trackpieces in range(30):
			self.road += self.straight
		self.road += self.right
		for trackpieces in range(25):
			self.road += self.straight
		self.road += self.left
		for trackpieces in range(30):
			self.road += self.straight
		#TRACK2
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.right
		self.road += self.left
		self.road += self.right
		for trackpieces in range(20):
			self.road += self.straight
		self.road += self.left
		for trackpieces in range(30):
			self.road += self.straight
		self.road += self.right
		for trackpieces in range(40):
			self.road += self.straight
		self.road += self.left
		self.road += self.right
		self.road += self.left
		self.road += self.right
		self.road += self.left
		for trackpieces in range(40):
			self.road += self.straight
		#TRACK3
		for trackpieces in range(30):
			self.road += self.straight
		self.road += self.left
		for trackpieces in range(30):
			self.road += self.straight
		self.road += self.right
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.left
		self.road += self.right
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.left
		self.road += self.right
		for trackpieces in range(30):
			self.road += self.straight
		self.road += self.right
		for trackpieces in range(15):
			self.road += self.straight
		self.road += self.left
		#TRACK4
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.right
		self.road += self.left
		for trackpieces in range(20):
			self.road += self.straight
		self.road += self.right
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.left2
		self.road += self.right
		for trackpieces in range(5):
			self.road += self.straight
		self.road += self.left2
		self.road += self.right2
		for trackpieces in range(30):
			self.road += self.straight
		self.road += self.right2
		for trackpieces in range(25):
			self.road += self.straight
		self.road += self.left
		self.road += self.left
		for trackpieces in range(45):
			self.road += self.straight
		#TRACK5
		self.road += self.right2
		for trackpieces in range(20):
			self.road += self.straight
		self.road += self.right2
		self.road += self.left2
		for trackpieces in range(20):
			self.road += self.straight
		self.road += self.left2
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.left2
		for trackpieces in range(15):
			self.road += self.straight
		self.road += self.right2
		for trackpieces in range(40):
			self.road += self.straight
		self.road += self.right2
		for trackpieces in range(35):
			self.road += self.straight
		self.road += self.left2
		self.road += self.right2
		for trackpieces in range(45):
			self.road += self.straight
		self.road += self.left
		'''
		#TRACK6
		self.road += self.right
		self.road += self.left
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.right3
		self.road += self.left3
		self.road += self.right3
		self.road += self.left3
		self.road += self.right3
		self.road += self.left3
		for trackpieces in range(5):
			self.road += self.straight
		self.road += self.left2
		for trackpieces in range(5):
			self.road += self.straight
		self.road += self.left2
		self.road += self.right3
		self.road += self.left
		self.road += self.right2
		for trackpieces in range(15):
			self.road += self.straight
		self.road += self.right
		for trackpieces in range(5):
			self.road += self.straight
		self.road += self.left3
		self.road += self.right3
		self.road += self.left3
		self.road += self.right3
		self.road += self.left3
		for trackpieces in range(15):
			self.road += self.straight
		self.road += self.left2
		self.road += self.right
		for trackpieces in range(10):
			self.road += self.straight
		self.road += self.right2
		self.road += self.left3
		self.road += self.right
		self.road += self.left2
		for trackpieces in range(30):
			self.road += self.straight

		#save created data to a text file with the appropriate track name
		file=open('data/tracks/track6.txt','w+')
		file.write(self.road)
		file.close()
