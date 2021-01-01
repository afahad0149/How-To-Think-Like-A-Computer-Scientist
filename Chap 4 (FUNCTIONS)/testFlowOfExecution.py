import turtle

def multicolor_square (t, sz):
	"""Make turtle t draw multi-colored squares of size sz"""
	for i in ["red", "purple", "hotpink", "blue"]: #error colors as undefined variables and not strings
		t.color(i)
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)

size = 20

for i in range (15):
	multicolor_square(alex,size) # error only occurs when function is called
	size = size + 10
	alex.forward(10)
	alex.right(18)

wn.mainloop()