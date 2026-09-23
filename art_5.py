from turtle import *

def draw_shape(color):
    penup()
    pendown()
    begin_fill()
    color(color)
    fd(20)
    lt(59)
    fd(56)
    rt(59)
    end_fill()
    penup()
    setposition(0, 0)
    rt(45)


def draw_shapes():
    speed(0)
    for i in range(8):
        draw_shape("navy")
        for i in range(2):
            draw_shape("light blue")

draw_shapes()
rt(45)
