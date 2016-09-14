import turtle

def draw_regular_polygon():
	sides = int(input("Choose how many sides you want your shape to have (must be greater than 2, less than 13): "))
	print(sides)
	#a = [3, 4, 5, 6 , 7, 8, 9 , 10, 11, 12]
	if sides not in range(3,13):
		print("You entry was invalid.")
		exit()
	else:
		window = turtle.Screen()
		window.bgcolor("grey")
		johnny = turtle.Turtle()
		johnny.shape('turtle')
		johnny.color('yellow')
		
		angle_sum = 180 * (sides - 2)
		print(angle_sum)
		angle = angle_sum / sides
		print(angle)
		for i in range(sides):
			print(angle)
			johnny.forward(100)
			johnny.right(180 - angle)
		window.exitonclick()

draw_regular_polygon()
