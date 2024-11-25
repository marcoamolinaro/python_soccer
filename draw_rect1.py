import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.speed(1)

pen.begin_fill()
pen.fillcolor("red")

pen.penup()
pen.goto(-300, -250)
pen.pendown()

pen.forward(600)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(600)
pen.left(90)
pen.forward(200)
pen.left(90)

pen.end_fill()
screen.exitonclick()