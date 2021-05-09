import turtle               # Tess becomes a traffic light

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
rose = turtle.Turtle()
liz = turtle.Turtle()

#repositioning turtles
tess.penup()
tess.goto(-50,-175)
tess.pendown()

alex.penup()
alex.goto(-50,-175)
alex.pendown()

rose.penup()
rose.goto(-50,-175)
rose.pendown()

liz.penup()
liz.goto(-50,-175)
liz.pendown()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(275)
    tess.circle(40, 180)
    tess.forward(275)
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

liz.penup()
#Position liz onto the place where the green+orange light should be
liz.forward(40)
liz.left(90)
liz.forward(50+70)
#Turn liz into a big black circle to show that it is initially off
liz.shape("circle")
liz.shapesize(3)
liz.fillcolor("black")


alex.penup()
#Position alex onto the place where the orange light should be
alex.forward(40)
alex.left(90)
alex.forward(50+140)
#Turn alex into a big black circle to show that it is initially off
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("black")

rose.penup()
#Position rose onto the place where the red light should be
rose.forward(40)
rose.left(90)
rose.forward(50+210)
#Turn tess into a big black circle to show that it is initially off
rose.shape("circle")
rose.shapesize(3)
rose.fillcolor("black")


# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():        
    global state_num
    if state_num == 0:              # Transition from state 0 to state 1
        tess.fillcolor("black")
        liz.fillcolor("#FFBF79")    # green+orange shade Hexcode
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1:            # Transition from state 1 to state 2
        liz.fillcolor("black")
        alex.fillcolor("orange")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 2:            # Transition from state 1 to state 2
        alex.fillcolor("black")
        rose.fillcolor("red")
        state_num = 3
        wn.ontimer(advance_state_machine, 2000)
    else:                           # Transition from state 2 to state 0
        rose.fillcolor("black")
        tess.fillcolor("green")       
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)
        
    

# Bind the event handler to the space key
wn.ontimer(advance_state_machine, 3000)

wn.mainloop()
