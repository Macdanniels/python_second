
# This program assigns random numbers to
# a two-dimensional list.
import random

def main():
    row = 4
    col = 2
    sum = 1
    

    #sample pattern of an empty two dimensional list
    two = [[0,0],
              [0,0],
              [0,0],
              [0,0]]
        
# Fill the list with random numbers.
    for i in range (row):
        for j in range (col):
            sum +=i
            two[i][j] += sum  
            print(two[i][j]*10)
        # print(two)

    # for 1,2,10,20....

           # values[i][j] = random.randint(1,100)
         #for printing in different lines   
             

    # Display the random numbers.
    # print(values)
    # print(values[0][3])


main()