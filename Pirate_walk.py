import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()

pirate.penup()
pirate.forward(100)

pirate.pendown()
angle = [160, -43, 270, -97, -43, 200, -940, 17, -86]
current_heading = 0


for a in angle:
    if (a >= 0):
        pirate.left(abs(a))
    else:
        pirate.right(abs(a))
    pirate.forward(100)
    current_heading = (current_heading + a) % 360
    
print(current_heading)
