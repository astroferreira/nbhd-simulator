from constants import *

class Object:


	def __init__(self, canvas=None, xpos=0, ypos=0, char='0'):
		self.xpos = xpos
		self.ypod = ypos
		self.last_xpos = xpos
		self.last_ypos = ypos
		self.char = char
		self.canvas = canvas
		self.draw(COLOUR_WHITE)


	def draw(self, color):

		last_position = (self.last_xpos, self.last_ypos)
		current_position = (self.xpos, self.ypos)

		if(current_position != last_position):
			self.canvas.screen.print_at(' ', self.last_xpos, self.last_ypos)

		self.canvas.screen.print_at(self.char, self.xpos, self.ypos, color)
		self.canvas.screen.refresh()