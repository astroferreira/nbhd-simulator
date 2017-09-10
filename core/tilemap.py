from constants import *
from stats.random import perlin
from entities.object import *

class TileMap:

	tilemap = None

	def __init__(self, screen=None):

		self.screen = screen
		self.map = perlin()
		self.generate_tilemap()
		self.screen.draw_world()

	def generate_tilemap(self):

		TileMap.tilemap = np.empty(shape=self.map.shape, dtype=Object)
		
		for i, row in enumerate(self.map):
			for j, tile in enumerate(row):
				tileposition = Position((i*TILE_SIZE, j*TILE_SIZE), 0)
				
				TileMap.tilemap[i, j] = Object(position=tileposition, screen=self.screen, filename=TILE_LIST[tile])


	def get_at(x, y):

		x = int((x-TILE_SIZE)/TILE_SIZE)
		y = int((y-TILE_SIZE)/TILE_SIZE)
		#print(x, y)

		return TileMap.tilemap[x, y]


