
#A program that collects a reference numbers via the function that collects the numbers 

def origin():
    
    numbers = get_references()

    # Display the values in the list.
    print('The numbers in the list are:')
    print(numbers)
    
   


def get_references():


  #create empty list.....................
    values = []

    # Create a variable to control the loop.
    try_again = 'y'

    while try_again == 'y':
        numbers = int(input('Enter the values: '))
        values.append(numbers)
        
        #inputing another value 
        print('Do you want to enter another value?')
        try_again = (input('y == yes: and n or any other entry == no: '))
        print()

    return values


origin()   
