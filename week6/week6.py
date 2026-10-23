import turtle

# -- setup --
wn = turtle.Screen()
wn.bgcolor("green")

tess = turtle.Turtle()

# -- function --

def draw_poly(someturtle,somesides,somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)
def drawspirel(someturtle,angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size = size + 2

def drawequitrinagle(someturtle,somesize):
    draw_poly(someturtle,3,somesize )
def drawstar(someturtle,somesize):
    for i in range(5):
        someturtle.forward(somesize)
        someturtle.right(144)




def drawsprite(someturtle, legs, lenght):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)
def drawsprite(someturtle, legs, lenght):
    angle = 360 / legs
    for i in range(legs):
        someturtle.forward(lenght)
        someturtle.backward(lenght)
        someturtle.left(angle)
# -- exercise --

# tess.pencolor("hotpink")
# tess.pensize(3)
# draw_poly(tess , 8 , 50)
# wn.exitonclick()
# -- finish --

# exercise 2
# tess.pencolor("blue")
# tess.pensize(2)
# for i in range(20):
#     draw_poly(tess , 4 , 100)
#     tess.left(18)
#finish

# exercise 3
# tess.color("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawspirel(tess,90)
#
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawspirel(tess,89)
# wn.exitonclick()

# exercise 4
# drawequitrinagle(tess, 100)
# wn.exitonclick()

# exercise 5
# tess.pencolor("red")
# for i in range(5):
#     drawstar(tess,50)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()


#     exercise 6
drawsprite(tess,legs=20,lenght=120)
wd.exitonclick()


# --finish --