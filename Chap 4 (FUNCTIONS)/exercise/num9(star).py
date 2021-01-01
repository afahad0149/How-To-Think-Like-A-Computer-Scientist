import turtle

def draw_star(t, sz):
	for i in range(5):
		t.forward(sz)
		t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tur = turtle.Turtle()
tur.color("hotpink")
tur.pensize(2)

draw_star(tur, 100)