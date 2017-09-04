from constants import *
import numpy as np


class Object:

	char = 'O'
	world_objects = []
	world_map = np.empty(shape=(100, 100), dtype=object)

	def __init__(self, canvas=None, xpos=0, ypos=0):
		self.xpos = xpos
		self.ypod = ypos
		self.last_xpos = xpos
		self.last_ypos = ypos
		self.canvas = canvas
		self.draw(COLOUR_WHITE)
		Object.world_objects.append(self)


	def draw(self, color):

		last_position = (self.last_xpos, self.last_ypos)
		current_position = (self.xpos, self.ypos)

		if(current_position != last_position):
			self.canvas.screen.print_at(' ', self.last_xpos, self.last_ypos)
			Object.world_map[self.last_xpos, self.last_ypos] = None

		self.canvas.screen.print_at(self.char, self.xpos, self.ypos, color)

		obj = self

		Object.world_map[self.xpos][self.ypos] = obj

		self.canvas.screen.refresh()

	def get_at(x, y):
		return Object.world_map[x][y]
