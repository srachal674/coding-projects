from turtle import*

speed(9)
#bgcolor("black")

length = 2
angle = 15
for i in range(10):
    begin_fill()
    color("blue")
    length = length + 1
    fd(length)
    rt(angle)
    for i in range(10):
        color("purple")
        length = length + 1
        fd(length)
        rt(angle)
        for i in range(10):
            color("red")
            length = length + 1
            fd(length)
            rt(angle)
            for i in range(10):
                color("orange")
                length = length + 1
                fd(length)
                rt(angle)
                for i in range(10):
                    color("yellow")
                    length = length + 1
                    fd(length)
                    rt(angle)
                    for i in range(10):
                        color("green")
                        length = length + 1
                        fd(length)
                        rt(angle)
                        angle = angle + 5
