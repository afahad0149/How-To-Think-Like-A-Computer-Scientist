import turtle

wn_color = input ("Enter desired color: ")
wn = turtle.Screen()
wn.bgcolor(wn_color)
wn.title("Hello Tess!")

tess = turtle.Turtle()
tess_color = input ("Enter turtle color: ")
tess.color(tess_color)
size = int (input("Enter pen size: "))
tess.pensize(size)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()