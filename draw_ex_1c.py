import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.penup()
pen.goto(40, 10)
pen.pendown()
pen.pensize(4)
pen.pencolor("green")
pen.left(90)
pen.forward(140)

screen.exitonclick()
