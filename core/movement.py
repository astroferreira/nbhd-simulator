import numpy as np
from constants import *
from entities.object import Position

def angle_orientation(dx, dy):

	if (dx == 0) and (dy ==0): 
		return 0

	angle = None

	null = unit_vector(np.array([0, -1]))
	displacement = unit_vector(np.array([dx, dy]))


	sign = [1, -1, 1]
	
	return sign[dx]*np.rad2deg(np.arccos(np.dot(null, displacement)))

def unit_vector(vector):
	return vector/np.linalg.norm(vector)


def possible_position(tilemap):

	grounds = np.where(tilemap == GROUND_TILE)

	position = np.random.randint(grounds[0].size+1)

	return Position((grounds[0][position]*TILE_SIZE, grounds[1][position]*TILE_SIZE), 0)

