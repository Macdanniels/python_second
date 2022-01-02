
#calculating average of test scores
# This program gets a series of test scores and
# calculates the average of the scores with the
# lowest score dropped

def origin():
    
    # Get the test scores from the user.
    scores = get_score()

    # Get the total of the test scores
    total = get_total(get_score())

    ## Get the lowest test score.
    lowest = min(scores)

    # Subtract the lowest score from the total.
    total -= lowest

    # Calculate the average. Note that we divide
    # by 1 less than the number of scores because
    # the lowest score was dropped.
    average = total / (len(scores) - 1)
    
    # Display the average.
    print('The average, with the lowest score dropped', 'is:' , average)


def get_score():
    
        
    #creating an empty list
    test_score = []


    again = 'y'

  
   #create a loop to control operations
    while again == 'y':
        
        # Get the scores from the user and add them to
        # the list.
        test_value = float(input('Enter the test score: '))
        # Get a score and add it to the list.
        test_score.append(test_value)

        #prompting user for decision
        print('Do you want to enter another score')
        again = input(' y = yes, anything else = no:')
        print()

        # Return the list.
    return test_score
    
                
def get_total(test_score_list):

    #create a accumulator

    total  = 0.0
    #calculating the total of list entered
    
    for numbers_intest in test_score_list:

        total += numbers_intest

    #resturning the total
    return total


origin()