
#check for status of number using normal program

try:
    number = int(input('Enter a number: '))
except ValueError:
    print("invalid input")
except NameError:
    print('Name Error!!')

if (number % 2) == 0:
    print(' The number is even.')
else:
    print('  The number is odd.')



#using function

# def mainfunction():

#     checker = int(input('Enter a number: '))
#     if is_even(checker):
#         print('The number is even.')
#     else:
#         print('The number is odd.')

# def is_even(number):
#     # Determine whether number is even. If it is,
# # set status to true. Otherwise, set status
# # to false.    
    
#     if (number % 2) == 0:
#         status = True
#     else:
#         status = False
# # Return the value of the status variable.
#     return status

# mainfunction()

