import turtle

wn = turtle.Screen()
wn.bgcolor ("green")

tortuga = turtle.Turtle()
tortuga.color("black", "blue")
tortuga.pensize(3)
tortuga.penup()

xs = [48, 117, 200, 240, 160, 260, 220]

def draw_bar (altura):
    tortuga.begin_fill()
    tortuga.forward(10)
    tortuga.left(90)
    tortuga.pendown()
    tortuga.forward(altura)
    tortuga.left(-90)
    tortuga.write(" "+str(altura))
    tortuga.forward(40)
    tortuga.left(-90)
    tortuga.forward(altura)
    tortuga.penup()
    tortuga.left(90)
    tortuga.end_fill()


for i in xs:
    if i >= 200:
        tortuga.color("black","red")
    elif i >= 100 and i < 200:
        tortuga.color("black", "yellow")
    elif i < 100:
        tortuga.color("black", "light green")
    draw_bar(i)
