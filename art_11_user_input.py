from turtle import*
from random import*

speed(0)
penup()

shape = textinput(title, prompt="Enter a dark color: ")
shapeLight = textinput(title, prompt="Enter a complementary light color: ")

def run():
    while True:
        design(shape, shapeLight)
        design(shape, shapeLight)
        if condition:
            break

#This will draw the shape
def design(shape, shape1Light):
    for i in range(10):
        for i in range(1):
            goto(randint(-500, 500), randint(-400,400))
            for i in range(8):
                for i in range(1):
                    pendown()
                    begin_fill()
                    color(shape)
                    fd(20)
                    lt(59)
                    fd(56)
                    rt(59)
                    end_fill()
                    penup()
                    rt(45)
                    for i in range(2):
                        pendown()
                        begin_fill()
                        color(shapeLight)
                        fd(20)
                        rt(59)
                        fd(56)
                        lt(59)
                        end_fill()
                        penup()
                        rt(45)
                        for i in range(1):
                            pendown()
                            begin_fill()
                            color(shape)
                            fd(20)
                            lt(59)
                            fd(56)
                            rt(59)
                            end_fill()
                            penup()
                            rt(45)
run()
