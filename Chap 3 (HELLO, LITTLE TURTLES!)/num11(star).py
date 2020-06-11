import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

for i in range(5):
	tess.forward(200)
	tess.right((2*360)//5)

tess.hideturtle()

wn.mainloop()