import turtle

def draw_square():
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


    window.exitonclick()

draw_square()
