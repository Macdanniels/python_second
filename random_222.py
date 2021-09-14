

import random


def rand_number():
    # global n
    # try:
    #     n.log(n)
    # except UnboundLocalError as error:
    #     n.log_exception(error)
    # except Exception as exception:
    #     n.log_exception(exception, False)

    #     print('Out of bound, enter a valid number')
       
    # except ValueError:
    #     print('Invalid Input, enter a number greater than 0')
    # except NameError:
    #     print('Invalid Input')
    n = int(input('how many random numbers: ')) 
    if (n < 0):
         return True
    list = []
    for x in range(n):
           list.append(random.randrange(1,n))
    print('The random numbers are: ')
    #array fotmat
    print(list)
    #normal format 
    print(*list, sep=' ,')
    print('\n')
    return list

    

rand_number()