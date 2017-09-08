import numpy as np

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



