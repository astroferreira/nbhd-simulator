from entities.object import *
import random_stats as random

class Wall(Object):

	char = 'W'

	def __init__(self, canvas, xpos=0, ypos=0):
		(self.xpos, self.ypos) = random.position()
		Object.__init__(self, canvas=canvas, xpos=self.xpos, ypos=self.ypos)