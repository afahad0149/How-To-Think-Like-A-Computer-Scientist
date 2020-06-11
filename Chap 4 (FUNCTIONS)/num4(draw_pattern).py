import turtle

def draw_square(t, sz):
	"""Draws a square od size sz"""

	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tur = turtle.Turtle()
tur.color("blue")
tur.pensize(3)

for i in range (20):
	draw_square(tur, 150)
	tur.right(360/20)

wn.mainloop()