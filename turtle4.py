import turtle

turtle.penup()
turtle.setpos(-50.00, 25.00)
turtle.pendown()
turtle.width(10)

def left_square(length) :
    n = 4
    turtle.color(colorin, colorout)
    turtle.begin_fill()
    while n:
        turtle.left(90)
        turtle.forward(length)
        n = n - 1
    turtle.end_fill()

while True:
    length = raw_input("How big would you like your square to be?") #getting the variable length from the user
    try:
        length = int(length)
        break
    except: 
        print "Please enter a number."

while True:
    colorout = raw_input("What color do you want the outside of your square to be: red, blue, or green?")
    if colorout in ("red", "blue", "green"):
        break
    else:
        print "Please enter red, blue, or green."
while True:
    colorin = raw_input("What color do you want the inside of your square to be: red, blue, or green?")
    if colorin in ("red", "blue", "green"):
        break
    else:
        print "Please enter red, blue, or green."
left_square(int(length)) #converting the variable length into an integer

turtle.penup()
turtle.setpos(15.00, 25.00)
turtle.pendown()

def right_triangle(tlength) :
    n = 3
    turtle.color(tcolorin, tcolorout)
    turtle.begin_fill()
    while n:
        turtle.left(120)
        turtle.forward(tlength)
        n = n -1
    turtle.end_fill()

while True:
    tlength = raw_input("How big would you like your triangle to be?") #getting the variable length from the user
    try:
        tlength = int(tlength)
        break
    except: 
        print "Please enter a number."

while True:
    tcolorout = raw_input("What color do you want the outside of your triangle to be: red, blue, or green?")
    if tcolorout in ("red", "blue", "green"):
        break
    else:
        print "Please enter red, blue, or green."
while True:
    tcolorin = raw_input("What color do you want the outside of your square to be: red, blue, or green?")
    if tcolorin in ("red", "blue", "green"):
        break
    else:
        print "Please enter red, blue, or green."
right_triangle(int(tlength))

turtle.exitonclick()
