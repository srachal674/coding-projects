from turtle import *

penup()
setposition(-250, 0)
pendown()

for i in range(10):
    begin_fill()
    color("navy")
    circle(30)
    end_fill()
    penup()
    forward(28)
    pendown()
    
