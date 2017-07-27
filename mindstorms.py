import turtle

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

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("black")
    angie.circle(100)

    pam = turtle.Turtle()
    pam.color("white")
    i = 0

    while (i < 3):
        pam.forward(300)
        pam.left(120)
        i = i + 1


    window.exitonclick()

draw_shapes()
