
# This program assigns random numbers to
# a two-dimensional list.
import random

def original():
    row = 3
    col = 4

    #sample pattern of an empty two dimensional list
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

# Fill the list with random numbers.
    for i in range (row):
        for j in range (col):
            values[i][j] = random.randint(1,100)
         #for printing in different lines   
            print(values[i][j])

    # Display the random numbers.
    print(values)
    # print(values[0][3])


original()