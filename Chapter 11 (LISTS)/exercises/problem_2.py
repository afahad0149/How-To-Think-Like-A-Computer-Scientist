import turtle

wn = turtle.Screen()

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")

# It creates only one turtle instance to which both alex and tess refer. 
# so changing the color of alex changes that of tess.

# Confirming

tess.forward(100)
tess.left(90)
alex.forward(100)
alex.left(90)

wn.mainloop()  # Theory confirmed!