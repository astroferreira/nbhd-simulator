import numpy as np
import time 

import random_stats as random
from entities.object import * 

from datetime import datetime

class Person(Object):

	char = 'P'

	health = 100
	humor = 100 
	hungry = 100 
	cold = 100 
	loneliness = 100
	time_of_death = ''
	needs = []	

	critical_messages = ["I'm not healthy",
						  "I'm in a bad mood",
						  "I'm hungry",
						  "I'm feeling cold",
						  "I'm feedling alone"]

	
	def __init__(self, canvas, xpos=0, ypos=0):
		(self.xpos, self.ypos) = random.position()
		Object.__init__(self, canvas=canvas, xpos=self.xpos, ypos=self.ypos)
		print('Creating Person at position {} x and {} y'.format(self.xpos, self.ypos))
		self.updateNeeds()
			
	
	def updateNeeds(self):
		self.needs = np.array([self.health, self.humor, 
							   self.hungry, self.cold,
							   self.loneliness])
		self.walk()
		self.draw(COLOUR_GREEN)

	def stateFeelings(self):
		self.updateNeeds()
		minimal = min(self.needs)
		if(minimal < 50):
			index = np.where(self.needs == min(self.needs))[0]
			#for i in index:

				#print(self.critical_messages[i])
		#else:
			#print("I'm fine.")

	def isAlive(self):
		if(self.health == 0):
			return False
		else:
			return True

	def loseHealth(self):
		self.health = self.health - 1
		if (self.health < 10):	
			self.time_of_death = datetime.today()

	def increaseHunger(self):
		self.hungry = self.hungry - 1

	def live(self):
		time.sleep(1/GAME_SPEED)
		if(self.isAlive()):
			self.stateFeelings()
			#self.loseHealth()
			self.increaseHunger()
		#else:
			#print("I died at {}".format(self.time_of_death))

	def walk(self):
		(dx, dy) = random.random_step()

		if Object.get_at(self.xpos+dx, self.ypos+dy):
			print('Ops! Colision.')
		else:
			self.last_xpos = self.xpos
			self.last_ypos = self.ypos
			self.xpos += dx
			self.ypos += dy

