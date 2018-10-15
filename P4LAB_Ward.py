# Nested Loops
# 26 Sept 2018
# CTI-110 P4HW3 - Nested Loops
# Kayla Ward
#

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("red")     # set pencolor (takes string)
t.shape("circle")

#commands from here to the last line can be replaced
# octagon, sides are 360 / 8 = 45 degrees
 
t.left(180)             # this time we'll draw it in a different direction

# draw a star by adding a triangle on to each side
# this uses nested loops

for i in (1,2,3,4,5,6,7,8):
    # turn the other direction, so the triangle's on the outside
    for j in (1,2,3,4):
        t.forward(100)
        t.right(90)
    t.forward(100)
    t.left(45)

# It looks like a flower!!


# end commands
win.mainloop()             # Wait for user to close window
