import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.pensize(4)

tess.penup()
tess.stamp()

for i in range(12):
	tess.forward(100)
	tess.pendown()
	tess.forward(10)
	tess.penup()
	tess.forward(25)
	tess.stamp()
	tess.backward(135)
	tess.left(360//12)

wn.mainloop()