import turtle

wn = turtle.Screen()
wn.bgcolor("green")
tortuga = turtle.Turtle

def sum_to(n):
    Soma = 0
    for i in range(n+1):
        Soma = Soma + i
    return Soma

##def Area_Circle (raio):
        ##pi = math.pi
        ##Area = pi*(raio**2)
        ##return Area

def draw_star (sz):
    global tortuga
    for i in range(5):
        tortuga.forward(sz)
        tortuga.left(-144)

for i in range (5):
    tortuga.forward(350)
    tortuga.pendown()
    draw_star(100)
    tortuga.penup()
    tortuga.left(-144)
