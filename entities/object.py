import pygame
import os
import time 

from constants import *
from stats import random
import numpy as np


class Object:

	world_objects = []

	def __init__(self, position=None, screen=None, filename=None, animated=False):
		
		if position is None:
			self.position = random.position()
		else:
			self.position = position

		self.last_position = self.position
		self.screen = screen
		self.animated = animated

		if filename is not None:
			self.filename = filename
			self.load()
			#self.draw()

		
		Object.world_objects.append(self)

	def load(self):
		self.image = pygame.image.load(os.path.join('assets', 'images', self.filename)).convert()
		self.rect = self.image.get_rect()
		self.image.set_colorkey((255,255,255))

	def move(self, dx, dy, angle):

		self.last_position = Position((self.position.x, self.position.y), self.position.angle)
		self.next_position = Position((self.position.x + dx, self.position.y + dy), angle)

		self.position = self.next_position
		self.rect.move_ip(self.position.x, self.position.y)

		#self.draw()
		#self.animate()


	def animate(self):
		
		for step_angle in np.linspace(self.last_position.angle, self.next_position.angle, 20):
			self.position.angle = step_angle
			self.screen.draw_world()

		for step_x, step_y in zip(np.linspace(self.last_position.x, self.next_position.x, 10), np.linspace(self.last_position.y, self.next_position.y, 10)):
			self.position.x = step_x
			self.position.y = step_y
			self.screen.draw_world()
				
					


	def draw(self):
		self.screen.surface.blit(self.rotate(self.position.angle), (self.position.x, self.position.y))


	def rotate(self, angle):
		self.position.angle = angle

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