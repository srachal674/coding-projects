from turtle import*

speed(0)
colors = ["blue","purple","red","orange","yellow","green"]
bgcolor("black")
for i in range(200):
    #Sets the pen color to rotate between the colors in the array through the loop iterations
    pencolor(colors[i%6])
    #Increases the width on each iteration.
    width(i/100 + 1)
    #Moves forward
    fd(i)
    #Turns left
    lt(59)
