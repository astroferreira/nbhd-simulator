import noise
import numpy as np

from constants import *
from entities.object import Position



def perlin(x=60, y=60):
 
   octaves = 1
   f = 5*np.random.rand(1) * octaves
   
   noise2D = np.array([noise.pnoise2(i/f, j/f, octaves) for j in range(y) for i in range(x)]).reshape((x, y))

   noise2D[noise2D > 0] = 1
   noise2D[noise2D <= 0] = 0

   return noise2D[0:50, 0:30].astype(int)



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






