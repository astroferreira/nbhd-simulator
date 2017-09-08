from constants import *
from entities.object import Position

import numpy as np


def position():

	x, y = SCREEN_RESOLUTION

	#theta = np.random.randint(360)
	coordinates = (np.random.randint(x), np.random.randint(y))

	return Position(coordinates, 0)

def step():

	step_x = np.random.randint(3)
	step_y = np.random.randint(3)

	dx = 0
	dy = 0

	if step_x == 1:
		dx += 1
	
	if step_x == 2:
		dx -= 1

	if step_y == 1:
		dy += 1
	
	if step_y == 2:
		dy -= 1

	return (dx, dy)






