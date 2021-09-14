
# This program displays five random
2 # numbers in the range of 1 through 100.
import random

def main_function():
    for count in range(5):
 # Get a random number.
        number = random.randint(1, 100)
# 7 Introduction to Value-Returning Functions: Generating Random Numbers  
# Display the number.
        print(number)
    

 # Call the main function.
main_function()