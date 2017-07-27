import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    turtle.shape("turtle")
    turtle.color("green")
    turtle.speed(3)
    i = 0

    while(i<4):
        brad.forward(100)
        brad.right(90)
        i = i + 1

    angie = turtle.Turtle()
    turtle.shape("arrow")
    turtle.color("black")
    angie.circle(100)


    window.exitonclick()

draw_shapes()
