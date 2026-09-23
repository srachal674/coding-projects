from turtle import*
from random import*

speed(0)
penup()

for i in range(10):
    for i in range(1):
        goto(randint(-500, 500), randint(-400,400))
        for i in range(8):
            for i in range(1):
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
                    for i in range(1):
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
    for i in range(1):
        goto(randint(-500, 500), randint(-400,400))
        for i in range(8):
            for i in range(1):
                pendown()
                begin_fill()
                color("purple")
                fd(20)
                lt(59)
                fd(56)
                rt(59)
                end_fill()
                penup()
                #setposition(-100,100)
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
                    #setposition(-100,100)
                    rt(45)
                    for i in range(1):
                        pendown()
                        begin_fill()
                        color("purple")
                        fd(20)
                        lt(59)
                        fd(56)
                        rt(59)
                        end_fill()
                        penup()
                        #setposition(-100,100)
                        rt(45)





