import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.penup()
pen.goto(-300, 50)
pen.pendown()
pen.pensize(2)
pen.pencolor("purple")
pen.forward(140)

screen.exitonclick()
