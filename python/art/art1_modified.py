from turtle import*
shape("turtle")
speed(0)
bgcolor("#f2f2f2")

colors = ["blue","purple","red","orange","yellow","green"]
small_radius = 50
med_radius = 75
lg_radius = 100
radi = [small_radius, med_radius, lg_radius]

for a in range(2):
    for c in colors:
        for r in radi:
                
            #Draw circles
            begin_fill()
            color(c)
            circle(r)
            right(50)
        
done()