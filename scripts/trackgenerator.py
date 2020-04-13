import pygame, sys
from pygame.locals import *
import numpy as np

class TrackGenerator:
	def __init__(self, x = None, y = None):
		self.straight = '3'
		self.left = '222222222222222222222222222222221111111111111111111111111111111144444444444444444444444444444444'
		self.right = '444444444444444444444444444444445555555555555555555555555555555522222222222222222222222222222222'
		self.blank = '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
		self.track = []
		self.road = ''
		self.sidelines = ''
		self.streetobjects = ''
	def generate(self):
		for trackpieces in range(25):
			self.road += self.straight
			self.sidelines += '1'
			self.streetobjects += '1'

		self.road += self.left
		self.sidelines += self.blank
		self.streetobjects += self.blank

		for trackpieces in range(25):
			self.road += self.straight
			self.sidelines += '1'
			self.streetobjects += '1'

		self.road += self.right
		self.sidelines += self.blank
		self.streetobjects += self.blank

		self.track.append(self.road)
		self.track.append(self.sidelines)
		self.track.append(self.streetobjects)

		file=open('tracks/track1.txt','w+')
		for element in self.track:
		     file.write(str(element))
		     file.write('\n')
		file.close()
