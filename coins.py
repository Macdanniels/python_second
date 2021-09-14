
# This program simulates 10 tosses of a coin.
import random 
# Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def main_function():

     for toss in range(TOSSES):
 # Simulate the coin toss.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')
            # print(random.uniform(0.1, 0.5))
# Call the main function.
main_function()