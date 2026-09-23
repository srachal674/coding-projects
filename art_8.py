from turtle import*
from random import randint

speed(0)
pensize(3)
colormode(255)

for i in range(20):
    begin_fill()
    color(randint(0,255),randint(0,255),randint(0,255))
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
        for i in range(1):
            rt(45)
            fd(150)
            rt(135)
            fd(150)
            rt(45)
            fd(150)
            rt(135)
            fd(150)
    penup()
    goto(randint(-500,500),randint(-300,300))
    pendown()
