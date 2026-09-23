from turtle import*

speed(0)
for i in range(8):
    for i in range(1):
        pendown()
        color("navy")
        fd(20)
        lt(59)
        fd(56)
        rt(59)        
        penup()
        setposition(0,0)
        rt(45)
        for i in range(2):
            pendown()
            color("light blue")
            fd(20)
            rt(59)
            fd(56)
            lt(59)            
            penup()
            setposition(0,0)
            rt(45)

pendown()
color("navy")
fd(20)
lt(59)
fd(56)
rt(59)
penup()
setposition(0,0)
rt(45)
