import turtle

def draw_poly(t, n, sz):
	"""draws a polygon of n sides"""

	for i in range(n):
		t.forward(sz)
		t.left(360/n)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

draw_poly(tess, 8, 50)

wn.mainloop()