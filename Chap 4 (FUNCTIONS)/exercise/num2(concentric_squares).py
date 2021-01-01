import turtle

def draw_square(t, sz):
	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tur = turtle.Turtle()
tur.color("hotpink")
tur.pensize(3)

size = 20

for i in range(5):
	draw_square(tur, size)
	size = size + 20
	tur.penup()
	tur.backward(10)
	tur.right(90)
	tur.forward(10)
	tur.left(90)
	tur.pendown()

wn.mainloop()


