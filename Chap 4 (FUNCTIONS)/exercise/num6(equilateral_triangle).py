import turtle

def draw_poly(t, n, sz):
	"""draws a polygon of n sides"""

	for i in range(n):
		t.forward(sz)
		t.left(360/n)

def draw_equitriangle(t,sz):
	"""draws an equilateral triangle of size sz"""

	draw_poly(t, 3, sz)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

draw_equitriangle(tess, 150)

wn.mainloop()