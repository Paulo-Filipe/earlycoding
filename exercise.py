
import turtle

wn = turtle.Screen()
wn.bgcolor("green")
tortuga = turtle.Turtle()
tortuga.color("white")
Lado_Base = 0
total = 0
def draw_line (sz, angle):
        tortuga.forward(sz)
        tortuga.left(angle)
        
def Draw_Reg_Poly(t, n, sz):
    t = turtle.Turtle()
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def Draw_Equi_Triangle (t,sz):
    Draw_Reg_Poly(t,3,sz)

def sum_to(n):
    total = 0
    for i in range(n+1):
        total = total + 1
    return total

B = sum_to(10)
print(B)

        
        

