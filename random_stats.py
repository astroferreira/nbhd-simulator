from constants import *

import numpy as np

def position():

	initial_height = HEADER_HEIGHT + 1

	xpos = np.random.randint(MAX_MAPBOX)
	ypos = initial_height + np.random.randint(MAX_MAPBOX)

	return (xpos, ypos)


def random_step():

	step_x = np.random.randint(2)
	step_y = np.random.randint(2)

	dx = 0
	dy = 0

	if step_x == 1:
		dx += 1
	else:
		dx -= 1

	if step_y == 1:
		dy += 1
	else:
		dy -= 1
		
	return (dx, dy)






