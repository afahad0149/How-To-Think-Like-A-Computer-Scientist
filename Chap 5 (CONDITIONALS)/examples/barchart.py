import turtle

def draw_bar(t, height):
	t.begin_fill()
	t.left(90)
	t.forward(height)
	t.write (" " + str(height))
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
alex.color("blue", "red")
alex.pensize(3)

data = [48, 117, 200, 240, 160, 260, 220]

for i in data:
	draw_bar(alex, i)

wn.mainloop()