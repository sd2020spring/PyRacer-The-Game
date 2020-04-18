import pygame, sys
from pygame.locals import *
import numpy as np

class TrackGenerator:
	def __init__(self, x = None, y = None):
		self.straight = '3'
		self.left = '222222222222222222222222222222221111111111111111111111111111111144444444444444444444444444444444'
		self.left2 = '222222222222222211111111111111114444444444444444'
		self.left3 = '222222221111111144444444'
		self.right = '444444444444444444444444444444445555555555555555555555555555555522222222222222222222222222222222'
		self.right2 = '444444444444444455555555555555552222222222222222'
		self.right3 = '444444445555555522222222'
		self.track = []
		self.road = ''
	def generate(self):
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

		self.track.append(self.road)

		file=open('tracks/track6.txt','w+')
		for element in self.track:
		     file.write(str(element))
		     file.write('\n')
		file.close()
