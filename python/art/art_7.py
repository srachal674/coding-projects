from turtle import*

speed(0)
colors = ["navy","blue","light blue","purple","pink","red","orange","yellow","green",]

for i in range(8):
    begin_fill()
    color(colors[i%9])
    for i in range(1):
        lt(90)
        fd(200)
        rt(135)
        fd(200)
        lt(45)
        fd(200)
        rt(135)
        fd(200)
        lt(45)
        fd(200)
        rt(135)
        fd(200)
        lt(45)
        fd(200)
        rt(135)
        fd(200)
    end_fill()
