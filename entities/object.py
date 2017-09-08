import pygame
import os
import time 

from constants import *
from stats import random
import numpy as np


class Object:

	world_objects = []
	world_map = np.empty(shape=SCREEN_RESOLUTION, dtype=object)

	def __init__(self, position=None, screen=None, filename=None):
		
		if position is None:
			self.position = random.position()

		self.last_position = self.position
		self.screen = screen

		if filename is not None:
			self.filename = filename
			self.load()
			self.draw()

		
		Object.world_objects.append(self)

	def load(self):
		self.image = pygame.image.load(os.path.join('assets', 'images', self.filename)).convert()
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.image.set_colorkey((255,255,255))

	def move(self, dx, dy, angle):

		self.last_position = Position((self.position.x, self.position.y), self.position.angle)
		
		self.position.x += dx
		self.position.y += dy 
		
	
		self.position.angle = angle	

		self.screen.draw_world()

	def draw(self, animated=True):

		if animated:

			rotated_image = None
			
			for step_angle in np.linspace(self.last_position.angle, self.position.angle, 20):
				self.screen.clear()
				time.sleep(0.025)
				rotated_image = self.rotate(step_angle)
				self.screen.surface.blit(rotated_image, (self.last_position.x, self.last_position.y))
				pygame.display.flip()

			for step_x, step_y in zip(np.linspace(self.last_position.x, self.position.x, 10), np.linspace(self.last_position.y, self.position.y, 10)):
				self.screen.clear()
				time.sleep(0.05)
				self.screen.surface.blit(rotated_image, (step_x, step_y))
				pygame.display.flip()
					
		else:
			self.screen.surface.blit(self.rotate(self.position.angle), (self.position.x, self.position.y))


	def rotate(self, angle):
		#dtheta = self.position.angle - self.last_position.angle

		center = self.image.get_rect().center
		rotated_image = pygame.transform.rotate(self.image, angle)
		rotated_image.get_rect().center = center
		return rotated_image
		
	def get_at(x, y):
	 	return Object.world_map[x][y]


class Position:

	def __init__(self, coordinates, angle):
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.angle = angle

	def __str__(self):
		return "{} x-axis {} y-axis".format(self.x, self.y)