from turtle import *
from random import randint

shape("turtle")
speed(6)
pensize(3)
colormode(255)

def set_window_size():
    screensize()
    window_width, window_height = screensize()
    setworldcoordinates(-window_width/2, -window_height/2, window_width/2, window_height/2)

set_window_size()

def stop_loop():
    global running
    running = False

onscreenclick(stop_loop)  # Stop on mouse click)
listen()

running = True

while running:
    begin_fill()
    color(randint(0, 255), randint(0, 255), randint(0, 255))
    end_fill()
    for i in range(1):
        lt(45)
        fd(150)
        lt(135)
        fd(150)
        lt(45)
        fd(150)
        lt(135)
        fd(150)
        end_fill()
        for j in range(1):
            rt(45)
            fd(150)
            rt(135)
            fd(150)
            rt(45)
            fd(150)
            rt(135)
            fd(150)
    begin_fill()
    color(randint(0, 255), randint(0, 255), randint(0, 255))
    for k in range(1):
        rt(135)
        fd(150)
        rt(45)
        fd(150)
        rt(135)
        fd(150)
        rt(45)
        fd(150)
        end_fill()
    for l in range(1):
            lt(135)
            fd(150)
            lt(45)
            fd(150)
            lt(135)
            fd(150)
            lt(45)
            fd(150)
    penup()
    goto(randint(-int(window_width()/2), int(window_width()/2)), randint(-int(window_height()/2), int(window_height()/2)))
    pendown()
