import turtle

def draw_square(t, sz):
	for i in range(4):
		t.forward(20)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tur = turtle.Turtle()
tur.color("hotpink")

for i in range(5):
	draw_square(tur, 20)
	tur.penup()
	tur.forward(40)
	tur.pendown()