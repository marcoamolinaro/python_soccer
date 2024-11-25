import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.speed(1)

pen.begin_fill()
pen.fillcolor("blue")

pen.penup()
pen.goto(-100, -200)
pen.pendown()

pen.circle(200)

pen.end_fill()
screen.exitonclick()