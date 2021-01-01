#drawing the house 

import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

directions = [(180, 100), (-90, 100), (-30, 100), (-120, 100), (-120, 100),
				(135, 20000**0.5), (135, 100), (135, 20000**0.5)]
for (angle, distance) in directions:
	tess.left(angle)
	tess.forward(distance)

tess.penup()
tess.right(45)
tess.forward(100)

wn.mainloop()