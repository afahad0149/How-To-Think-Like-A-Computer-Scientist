import turtle

def draw_spiral(t, n, ang):
	size = 3
	for i in range(n):	
		t.forward(size)
		t.right(ang)
		size = size + 3



wn = turtle.Screen()
wn.bgcolor("lightgreen")

tur = turtle.Turtle()
tur.color("blue")

tur.penup()
tur.setx(-200)
tur.pendown()

draw_spiral(tur, 100, 90)

tur.penup()
tur.setpos(0,0)
tur.setx(200)
tur.pendown()

draw_spiral(tur, 100, 89)

wn.mainloop()