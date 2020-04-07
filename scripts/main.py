import pygame, sys
from pygame.locals import *
import numpy as np
import random
import time
from player import Player
from road import Road
from tree import Tree

WIDTH = 800
HEIGHT = 500

def main():
	pygame.init()
	pygame.display.set_caption('PyRacer')
	tilt = 0

	ingame = True
	DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
	WHITE = (255, 255, 255)
	BLACK = (0,0,0)
	GRAY = (50,50,50)
	DISPLAY.fill(BLACK)
	background = pygame.transform.scale(pygame.image.load('images/backgrounds/background3.png'), (WIDTH,HEIGHT))


	street = Road()

	#change first number to change car
	racer = Player(1, 30, 30, WIDTH/2, 7*HEIGHT/8 - 20)

	i = 0
	tree = np.zeros(500, dtype=object)
	while i < 500:
		tree[i] = Tree(0,0,0,WIDTH/2-20,HEIGHT/2+45)
		tree[i+1] = Tree(1,0,0,WIDTH/2+10,HEIGHT/2+45)
		i += 2
	print(tree)


	while True:
		DISPLAY.blit(background, (0,-100))
		print(street.distance)

		street.readtrack()
		street.update()
		tree[street.objectset].update()
		tree[street.objectset+1].update()
		racer.move()
		font = pygame.font.Font('freesansbold.ttf', 32)
		text = font.render(('SPEED: ' + str(round((street.speed/6.5)*18000)) + ' km/h'), True, WHITE, BLACK)
		textbox = text.get_rect()
		textbox.top = 10
		textbox.left = 10

		if street.accelerate:
			if street.tilt == 0:
				racer.dxs = 0
			elif street.tilt == -1:
				racer.dxs = 2*((street.speed+.3)*5)
			elif street.tilt == 1:
				racer.dxs = -2*((street.speed+.3)*5)
		else:
			racer.dxs = 0

		tree[street.objectset].dscaleby = street.speed*10
		tree[street.objectset].dx = (410*street.speed - street.tilt*street.speed)
		tree[street.objectset+1].dscaleby = street.speed*10
		tree[street.objectset+1].dx = (340*street.speed + street.tilt*street.speed)



		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				#player moves left when left key is pressed
				if event.key == pygame.K_LEFT:
					racer.dx = -5
					racer.image = racer.imgleft
				#player moves right when right key is pressed
				if event.key == pygame.K_RIGHT:
					racer.dx = 5
					racer.image = racer.imgright
				#player moves up when up key is pressed
				if event.key == pygame.K_UP:
					street.accelerate = True
					street.sp = .001
				#player moves down when down key is pressed
				if event.key == pygame.K_DOWN:
					street.reverse = True
					street.sp = -.004
			if event.type == pygame.KEYUP:
				#player stops moving left
				if event.key == pygame.K_LEFT:
					racer.dx = 0
					racer.image = racer.img
				#player stops moving right
				if event.key == pygame.K_RIGHT:
					racer.dx = 0
					racer.image = racer.img
				#player stops moving up
				if event.key == pygame.K_UP:
					 street.accelerate = False
					 street.sp = -.001
				#player stops moving down
				if event.key == pygame.K_DOWN:
					 street.reverse = False
					 street.sp = 0

		#print('speed: ' + str(street.speed) + ' dtree: ' + str(tree1.dscaleby))
		DISPLAY.blit(racer.image, (racer.x-15,racer.y-15))
		DISPLAY.blit(text, textbox)

		#the following line continously calls the while loop
		pygame.display.update()

#the following line calls the main function and starts the game
main()
