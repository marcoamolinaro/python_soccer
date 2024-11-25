import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.penup()

pen.speed(2)

pen.goto(-300, -200)
pen.pendown()
pen.begin_fill()
pen.fillcolor("green")
pen.forward(600)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.forward(600)
pen.left(90)
pen.forward(400)
pen.end_fill()

pen.penup()
pen.goto(-300, 193.5)
pen.begin_fill()
pen.pencolor("black")
pen.pendown()
pen.fillcolor("black")
pen.circle(5)
pen.end_fill()

pen.goto(-300, -193.5)
pen.begin_fill()
pen.pencolor("white")
pen.pendown()
pen.fillcolor("white")
pen.circle(5)
pen.end_fill()

pen.penup()
pen.goto(290, -193.5)
pen.begin_fill()
pen.pencolor("blue")
pen.pendown()
pen.fillcolor("blue")
pen.circle(5)
pen.end_fill()

pen.penup()
pen.goto(290, 193.5)
pen.begin_fill()
pen.pencolor("yellow")
pen.pendown()
pen.fillcolor("yellow")
pen.circle(5)
pen.end_fill()


screen.exitonclick()