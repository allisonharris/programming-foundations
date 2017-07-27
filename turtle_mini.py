import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("#42dff4")

    sam = turtle.Turtle()
    sam.shape("circle")
    sam.speed(20)
    sam.color("white")

    for i in range (1,37):
        draw_square(sam)
        sam.right(10)

    for i in range(37,38):
        sam.right(90)
        sam.forward(350)

draw_flower()
    
turtle.exitonclick()


