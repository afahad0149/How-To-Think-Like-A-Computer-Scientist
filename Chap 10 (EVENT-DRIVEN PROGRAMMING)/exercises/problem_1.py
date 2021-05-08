import turtle

turtle.setup(400,500) # Determine the window size
wn = turtle.Screen() # Get a reference to the window
wn.title("Handling keypresses!") # Change the window title
wn.bgcolor("lightgreen") # Set the background color
tess = turtle.Turtle() # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye() # Close down the turtle window

def h5():
    tess.color('red')

def h6():
    tess.color('green')

def h7():
    tess.color('blue')

def h8():
    global size
    if size < 20:
        size += 1
        tess.pensize(size)

def h9():
    global size
    if size > 1:
        size -= 1
        tess.pensize(size)

def h10():
    turtle.setup(800,1000)

def h13():
    turtle.setup(400,500)

def h11():
    turtle.undo()


# These lines "wire up" keypresses to the handlers we've defined.

size = 1
shape = 0

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, 'r')
wn.onkey(h6, 'g')
wn.onkey(h7, 'b')
wn.onkey(h8, 'plus')
wn.onkey(h9, 'minus')
wn.onkey(h10, 'Return')
wn.onkey(h13, 'Delete')
wn.onkey(h11, 'Control_L')
wn.onkey(h4, 'Escape')
#wn.onkey(h12, 'Alt_L')



# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
