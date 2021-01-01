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
tur.penup()
tur.setpos(-100,100)
tur.pendown()

for i in range(5):
	draw_star(tur, 100)
	tur.penup()
	tur.forward(350)
	tur.pendown()
	tur.right(144)