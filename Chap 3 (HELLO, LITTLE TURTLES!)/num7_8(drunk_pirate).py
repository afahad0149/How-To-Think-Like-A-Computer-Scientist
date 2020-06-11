import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

head = 0
turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in turns:
	tess.left(i)
	head += i
	tess.forward(100)

head = head % 360

print ("heading =", head)
