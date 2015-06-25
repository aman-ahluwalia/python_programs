import turtle

def draw_art(some_turtle):
	i = 4
	while(i>0):
		some_turtle.forward(100)
		some_turtle.right(90)
		i = i-1


def draw_circle():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	brad.speed(8)
	for i in range (40):
		draw_art(brad)
		brad.right(10)
	window.exitonclick()

draw_circle()
