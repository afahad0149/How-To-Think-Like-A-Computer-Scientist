#drawing the drunk pirate's whimsical route

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle, distance) in data:
	alex.left(angle)
	alex.forward(distance)

wn.mainloop()