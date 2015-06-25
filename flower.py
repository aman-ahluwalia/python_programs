import turtle

def draw_rhombus(some_turtle):
	some_turtle.forward(100)
	some_turtle.left(45)
	some_turtle.forward(100)
	some_turtle.left(135)
	some_turtle.forward(100)
	some_turtle.left(45)
	some_turtle.forward(100)

def set_start(some_turtle):
	some_turtle.penup()
	some_turtle.setpos(0,90)
	some_turtle.pendown()

def set_turtle(some_turtle):
	some_turtle.shape("turtle")
	some_turtle.color("blue")
	some_turtle.speed(8)

def draw_flower():
	window = turtle.Screen()
	window.bgcolor("pink")

	brad = turtle.Turtle()
	set_turtle(brad)
	set_start(brad)
	for i in range(72):
		draw_rhombus(brad)
		brad.left(130)
	brad.right(90)
	brad.forward(300)

	window.exitonclick()

draw_flower()
