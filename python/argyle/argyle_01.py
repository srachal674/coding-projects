import turtle
from random import randint

turtle.shape("turtle")
turtle.speed(6)
turtle.pensize(3)
turtle.colormode(255)

def set_window_size():
    screen = turtle.Screen()
    width = screen.window_width()
    height = screen.window_height()
    turtle.setworldcoordinates(-width/2, -height/2, width/2, height/2)
    return width, height

window_width, window_height = set_window_size()

try:
    while True:
        turtle.begin_fill()
        turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.end_fill()
        for i in range(1):
            turtle.lt(45)
            turtle.fd(150)
            turtle.lt(135)
            turtle.fd(150)
            turtle.lt(45)
            turtle.fd(150)
            turtle.lt(135)
            turtle.fd(150)
            
            for j in range(1):
                turtle.rt(45)
                turtle.fd(150)
                turtle.rt(135)
                turtle.fd(150)
                turtle.rt(45)
                turtle.fd(150)
                turtle.rt(135)
                turtle.fd(150)
            turtle.begin_fill()
            turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
            for k in range(1):
                turtle.rt(135)
                turtle.fd(150)
                turtle.rt(45)
                turtle.fd(150)
                turtle.rt(135)
                turtle.fd(150)
                turtle.rt(45)
                turtle.fd(150)
                turtle.end_fill()
                for l in range(1):
                    turtle.lt(135)
                    turtle.fd(150)
                    turtle.lt(45)
                    turtle.fd(150)
                    turtle.lt(135)
                    turtle.fd(150)
                    turtle.lt(45)
                    turtle.fd(150)
            turtle.penup()
            turtle.goto(randint(-int(window_width /2), int(window_width /2)), randint(-int(window_height /2), int(window_height /2)))
            turtle.pendown()
except turtle.Terminator:
    print("Drawing stopped.")
