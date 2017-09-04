from entities import Person as p
from entities import wall as w
from graphics import canvas as c
from entities import object as o
from time import sleep



canvas = c.Canvas()
person = p.Person(canvas)

for i in range(150):
	wall = w.Wall(canvas)

while(True):
	person.live()
