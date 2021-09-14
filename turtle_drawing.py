
import turtle


def main():
    turtle.hideturtle()                    
    square(100, 0, 50, 'red')  
    square(-150, -100, 200, 'blue')             
    square(-200, 150, 75, 'green')   
    
# 9 # The square function draws a square. The x and y parameters
# 10 # are the coordinates of the lower-left corner. The width
# 11 # parameter is the width of each side. The color parameter
# 12 # is the fill color, as a string.
 
def square(x, y, width, color):
    turtle.penup() # Raise the pen
    turtle.goto(x, y) # Move to the specified location
    turtle.fillcolor(color) # Set the fill color
    turtle.pendown() # Lower the pen
    turtle.begin_fill() # Start filling

    for count in range(4): # Draw a square
        turtle.forward(width)
        turtle.left(90)
        turtle.end_fill() # End filling

# Call the main function.
main()