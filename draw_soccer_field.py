import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.speed(2)

pen.penup()
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
pen.goto(0, -200)
pen.pendown()
pen.pensize(4)
pen.pencolor("white")
pen.left(180)
pen.forward(400)

pen.penup()
pen.goto(50, 0)
pen.pendown()
pen.circle(50)

pen.penup()
pen.goto(-300, 50)
pen.pendown()
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(50)

pen.penup()
pen.goto(300, 50)
pen.pendown()
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)

pen.penup()
pen.goto(0,0)
pen.pendown()
pen.dot(10)




screen.exitonclick()