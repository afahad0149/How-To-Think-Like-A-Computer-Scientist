import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 60) # h1 is called after every 60ms

#wn.ontimer(h1, 2000)       # h1 called only once
h1() #h1 called from main function
wn.mainloop()