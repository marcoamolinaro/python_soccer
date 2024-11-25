import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.speed(1)

pen.penup()
pen.goto(-150,0)
pen.pendown()
pen.pensize(2)
pen.pencolor("red")
pen.forward(200)

pen.penup()
pen.goto(0,-50)
pen.pendown()
pen.pensize(4)
pen.pencolor("blue")
pen.forward(150)

pen.penup()
pen.goto(100, 50)
pen.pendown()
pen.pensize(6)
pen.pencolor("green")
pen.forward(100)

screen.exitonclick()
