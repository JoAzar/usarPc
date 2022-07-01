import turtle
import keyboard

t = turtle.Turtle()
x=0
y=0
vuelta=0
cant=0
parImpar=1
t.speed(0)
t.fillcolor()
cerrar=True

while x<80 and cerrar==True:
    while vuelta<80:
        t.penup()
        t.goto(x, y+vuelta)
        t.pendown()
        if parImpar%2==0:
            t.begin_fill()
            for i in range(0, 4):
                t.forward(10)
                t.left(90)
            t.end_fill()
            parImpar=parImpar+1
        else:
            for i in range(0, 4):
                t.forward(10)
                t.left(90)
            parImpar=parImpar+1
        vuelta=vuelta+10
    x=x+10
    vuelta=0
    parImpar=parImpar+1
if keyboard.read_key() == "q":
    cerrar=False  



