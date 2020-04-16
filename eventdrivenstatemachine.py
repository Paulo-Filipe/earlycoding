import turtle # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tessO = turtle.Turtle()
tessR = turtle.Turtle()


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

def greentimer():
    advance_state_machine()
    wn.ontimer(quicktimer, 3000)
    
def quicktimer():
    advance_state_machine()
    wn.ontimer(orangetimer,1000)
    
def orangetimer():
    advance_state_machine()
    wn.ontimer(redtimer, 1000)
    
def redtimer():
    advance_state_machine()
    wn.ontimer(greentimer, 2000)
    
draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
tessO.forward(40)
tessO.left(90)
tessO.forward(120)
tessR.forward(40)
tessR.left(90)
tessR.forward(190)
# Turn tess into a big green circle
tess.shape("circle")
tessO.shape("circle")
tessR.shape("circle")
tessO.shapesize(3)
tessR.shapesize(3)
tess.shapesize(3)
tess.fillcolor("darkgreen")
tessO.fillcolor("darkorange")
tessR.fillcolor("darkred")


# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess’ position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tessR.fillcolor("darkred")
        tess.fillcolor("green")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tessO.fillcolor("orange")
        state_num = 2
    elif state_num == 2:# Transition from state 2 to state 3
        tess.fillcolor("darkgreen")
        tessO.fillcolor("orange")
        state_num = 3
    else: # Transition from state 3 to state 0
        tessO.fillcolor("darkorange")
        tessR.fillcolor("red")
        state_num = 0

# Bind the event handler to the space key.
wn.ontimer(greentimer, 100)

wn.listen() # Listen for events
wn.mainloop()
