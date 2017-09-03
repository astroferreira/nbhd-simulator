from constants import *
from asciimatics.screen import Screen
from time import sleep 

class Canvas:

	width = None
	height = None
	screen = None

	def __init__(self):
		self.screen = Screen.open()
		self.width = self.screen.width
		self.height = self.screen.height
		self.header()

	def print(self, message, x=0, y=0):
		self.screen.print_at(message, x, y)
		self.screen.refresh()

	def header(self):
		self.screen.print_at(HEADER_MAIN_MESSAGE.format(VERSION), 0, 0)
		self.screen.move(0, HEADER_HEIGHT)
		self.screen.draw(self.width, HEADER_HEIGHT)
		self.screen.refresh()

	def draw_map(self):

		width = self.screen.width/4
		height = self.screen.height/4



		self.screen.move(0, 0)
		self.screen.draw(width, 0)
		self.screen.draw(width, height)
		self.screen.move(0, height)
		self.screen.draw(width, height)
		self.screen.move(0, height)
		self.screen.draw(0, 0)
		self.screen.refresh()
		sleep(2)
		#self.screen.draw(0, 0)
