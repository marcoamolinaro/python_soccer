import turtle

def draw_ball(star, end, color, size):
    pen.penup()
    pen.goto(star, end)
    pen.begin_fill()
    pen.pencolor(color)
    pen.pendown()
    pen.fillcolor(color)
    pen.circle(size)
    pen.end_fill()
    
    
screen = turtle.Screen()

pen = turtle.Turtle()

pen.penup()

pen.speed(50)

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

draw_ball(-300, 193.5, "orange", 5)
draw_ball(-300, -193.5, "orange", 5)
draw_ball(290, -193.5, "orange", 5)
draw_ball(290, 193.5, "orange", 5)

draw_ball(-285, 193.5, "yellow", 5)
draw_ball(-285, -193.5, "yellow", 5)
draw_ball(275, -193.5, "blue", 5)
draw_ball(275, 193.5, "blue", 5)

draw_ball(-270, 193.5, "blue", 5)
draw_ball(-270, -193.5, "blue", 5)
draw_ball(260, -193.5, "yellow", 5)
draw_ball(260, 193.5, "yellow", 5)

draw_ball(5, 0, "black", 5)

screen.exitonclick()

