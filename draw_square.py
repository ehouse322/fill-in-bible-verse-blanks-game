import turtle

def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')
	#Create the turtle which will draw the square; named Tom
	tom = turtle.Turtle()
	tom.shape('turtle')
	tom.color('yellow')
	tom.speed(20)
	for i in range(1, 37):
		draw_square(tom)
		tom.right(10)

	window.exitonclick()

draw_art()
print('hello')