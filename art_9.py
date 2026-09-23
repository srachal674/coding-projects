from turtle import*
from random import*

speed(0)

def blueJax():    
    for i in range(7):
        for i in range(2):
            pendown()
            begin_fill()
            color("navy")
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
                color("light blue")
                fd(20)
                rt(59)
                fd(56)
                lt(59)
                end_fill()
                penup()
                rt(45)
                
def purpleJax():   
    for i in range(7):
        for i in range(2):
            pendown()
            begin_fill()
            color("purple")
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
                color("pink")
                fd(20)
                rt(59)
                fd(56)
                lt(59)
                end_fill()
                penup()
                rt(45)

for i in range(10):
    penup()
    goto(randint(-500, 500), randint(-300,300))
    blueJax()
    penup()
    goto(randint(-500, 500), randint(-300,300))
    purpleJax()
