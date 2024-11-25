import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.pensize(4)
pen.pencolor("purple")
pen.right(90)
pen.forward(140)

screen.exitonclick()
