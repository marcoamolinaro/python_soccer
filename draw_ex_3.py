import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.penup()
pen.goto(5, 0)
pen.begin_fill()
pen.pencolor("black")
pen.pendown()
pen.fillcolor("black")
pen.circle(30)
pen.end_fill()

pen.penup()
pen.goto(-25, 30)
pen.pendown()
pen.pensize(2)
pen.pencolor("yellow")
pen.forward(62)

pen.penup()
pen.goto(5, 60)
pen.right(90)
pen.pendown()
pen.pensize(2)
pen.pencolor("white")
pen.forward(62)

screen.exitonclick()