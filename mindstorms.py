import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(3)
    i = 0

    while(i<4):
        brad.forward(100)
        brad.right(90)
        i = i + 1

    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("black")
#    angie.circle(100)

#    pam = turtle.Turtle()
#    pam.color("white")
#    i = 0

#    while (i < 3):
#        pam.forward(300)
#        pam.left(120)
#        i = i + 1


    window.exitonclick()

draw_shapes()
