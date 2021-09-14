

# This program calculates the length of a right
 # triangle's hypotenuse.
import math

def main():
   
    hpo()

def hpo():
    
     # Get the length of the triangle's two sides.
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))
    radius = float(input('Enter the Radius of a circle: '))

 # Calculate the length of the hypotenuse.
    c = math.hypot(a, b)
    d = math.ceil(c)

 # Display the length of the hypotenuse.
    print('The length of the hypotenuse is', c , '\n', d)
    area_calculation(radius)
    

# Call the main function.

def area_calculation(radius):

    area = math.pi * radius**2
    print('The Area of the Cirle is:', area)
    return area
main()