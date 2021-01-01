import turtle

def draw_bar(t, height):
	if (height >= 200):
		t.color("blue", "red")
	elif (height >= 100):
		t.color("blue", "yellow")
	else:
		t.color("blue", "green")

	t.begin_fill()
	t.left(90)
	t.forward(height)
	if (height >= 0):
		t.write (" " + str(height))
	else:
		t.penup()
		t.right(180)
		t.forward(15)
		t.write (" " + str(height))
		t.forward(-15)
		t.left(180)
		t.pendown()
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.end_fill()
	t.penup()
	t.left(90)
	t.forward(10)
	t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)

data = [48, 117, 200, 240, 160, 260, 220, -100, -30, -250]

for i in data:
	draw_bar(alex, i)

wn.mainloop()