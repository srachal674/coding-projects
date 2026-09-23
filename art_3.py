from turtle import*

speed(6)
#width(3)
dist = 100
angle = 45
#length = dist + 4
penup()
for i in range(10):
    goto(-30, 50)
    pendown()
    color("blue")
    fd(dist)
    dist = dist - 2
    bk(dist)
    lt(angle)
    penup()
    #dist = dist - 2
    angle = angle - 1
    pendown()
    fd(dist)
    dist = dist - 2
    bk(dist)
    lt(angle)
    penup()
