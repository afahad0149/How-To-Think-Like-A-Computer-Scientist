import turtle
__import__("turtle").__traceable__ = False

def multicolor_square (t, sz):
	"""Make turtle t draw multi-colored squares of size sz"""
	for i in ["red", "purple", "hotpink", "blue"]:
		t.color(i)
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)

size = 20

for i in range (15):
	multicolor_square(alex,size)
	size = size + 10
	alex.forward(10)
	alex.right(18)

wn.mainloop()