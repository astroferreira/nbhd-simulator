from entities import Person as p
from graphics import canvas as c
from time import sleep


canvas = c.Canvas()
person = p.Person(canvas)
person2 = p.Person(canvas)

while(True):
	person.live()
	person2.live()