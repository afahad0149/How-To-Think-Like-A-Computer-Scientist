import turtle

wn = turtle.Screen() 
sam = turtle.Turtle()

#positioning
sam.penup()
sam.backward(250)
sam.pendown()

#equilateral triangle
for i in range (3):
	sam.forward(50)
	sam.left(360//3)

#positioning
sam.penup()
sam.forward(100)
sam.pendown()

#square
for i in range(4):
	sam.forward(50)
	sam.left(360//4)

#positioning
sam.penup()
sam.forward(150)
sam.pendown()

#hexagon
for i in range(6):
	sam.forward(50)
	sam.left(360//6)

#positioning
sam.penup()
sam.forward(200)
sam.pendown()

#octagon
for i in range(8):
	sam.forward(50)
	sam.left(360//8)
