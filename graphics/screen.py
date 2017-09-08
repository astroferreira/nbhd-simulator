import pygame

from constants import *
from entities.object import Object

class Screen:

	def __init__(self):

		pygame.init()

		self.surface = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.FULLSCREEN)
	

	def clear(self):
		self.surface.fill(ALPHA)

	def draw_world(self):
		
		self.clear()
		
		for object in Object.world_objects:
			object.draw()

		pygame.display.flip()


		
	# def print(self, message, x=0, y=0):
	# 	self.screen.print_at(message, x, y)
	# 	self.screen.refresh()

	# def header(self):
	# 	self.screen.print_at(HEADER_MAIN_MESSAGE.format(VERSION), 1, 1)
	# 	self.screen.move(0, HEADER_HEIGHT)
	# 	self.screen.draw(self.width, HEADER_HEIGHT)
	# 	self.screen.refresh()

	# def draw_map(self):

	# 	width = self.screen.width/4
	# 	height = self.screen.height/4



	# 	self.screen.move(0, 0)
	# 	self.screen.draw(width, 0)
	# 	self.screen.draw(width, height)
	# 	self.screen.move(0, height)
	# 	self.screen.draw(width, height)
	# 	self.screen.move(0, height)
	# 	self.screen.draw(0, 0)
	# 	self.screen.refresh()
	# 	sleep(2)
	# 	#self.screen.draw(0, 0)
