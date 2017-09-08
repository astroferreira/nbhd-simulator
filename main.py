import pygame

from pygame.locals import *
from os import sys
from time import sleep
from entities.person import Person
from entities.object import Object
from graphics.screen import Screen

screen = Screen()


screen.surface.fill((255, 255, 255))


o = Person(screen=screen)


clock = pygame.time.Clock()

while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type is KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()


	keys_pressed = pygame.key.get_pressed()

	# if keys_pressed[K_UP]:
	# 	o.move(0, -10, 0)				
	
	# if keys_pressed[K_DOWN]:
	# 	o.move(0, 10, 180)

	# if keys_pressed[K_LEFT]:
	# 	o.move(-10, 0, 270)

	# if keys_pressed[K_RIGHT]:
	# 	o.move(10, 0, 90)

	
	o.live()


	pygame.display.update()


