import pygame
import _thread

from pygame.locals import *
from os import sys
from time import sleep
from entities.person import Person
from entities.object import Object
from graphics.screen import Screen
from core.movement import *
from core.tilemap import TileMap

from stats.random import perlin


def game_loop(screen, mapa):

	clock = pygame.time.Clock()
	
	objects = []
	for i in range(1):
		objects.append(Person(screen=screen, position=possible_position(mapa.map), animated=True))
	
	#b = Person(screen=screen, position=possible_position(mapa.map), animated=True)
	
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type is KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()



		for o in objects:
			o.live()

		screen.draw_world()
		pygame.display.update()



screen = Screen()
mapa = TileMap(screen=screen)


game_loop(screen, mapa)


# 	keys_pressed = pygame.key.get_pressed()

# 	# if keys_pressed[K_UP]:
# 	# 	o.move(0, -10, 0)				
	
# 	# if keys_pressed[K_DOWN]:
# 	# 	o.move(0, 10, 180)

# 	# if keys_pressed[K_LEFT]:
# 	# 	o.move(-10, 0, 270)

# 	# if keys_pressed[K_RIGHT]:
# 	# 	o.move(10, 0, 90)

	


