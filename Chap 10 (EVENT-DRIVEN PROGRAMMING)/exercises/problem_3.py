import turtle               # Tess becomes a traffic light

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
rose = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
#Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
#Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

alex.penup()
#Position alex onto the place where the orange light should be
alex.forward(40)
alex.left(90)
alex.forward(50+70)
#Turn alex into a big orange circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("orange")

rose.penup()
#Position rose onto the place where the red light should be
rose.forward(40)
rose.left(90)
rose.forward(50+140)
#Turn tess into a big orange circle
rose.shape("circle")
rose.shapesize(3)
rose.fillcolor("red")

#Keep only green light on initially
alex.hideturtle()
rose.hideturtle()

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():        
    global state_num
    if state_num == 0:              # Transition from state 0 to state 1
        tess.hideturtle()
        alex.showturtle()
        state_num = 1
    elif state_num == 1:            # Transition from state 1 to state 2
        alex.hideturtle()
        rose.showturtle()
        state_num = 2
    else:                           # Transition from state 2 to state 0
        rose.hideturtle()
        tess.showturtle()        
        state_num = 0
        
    wn.ontimer(advance_state_machine, 2000)

# Bind the event handler to the space key
wn.ontimer(advance_state_machine, 2000)


wn.mainloop()
