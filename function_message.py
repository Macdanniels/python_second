

print('A function program that calculates sum of two numbers:')
print('lets get it started')

a1 = float(input('Please enter value for first value:' ))
operator = str(input('enter operator: ' ))
b1 = float(input('Please enter value for second value:' ))


def calculator(a,b):
    if(operator == "+"):
        add(a,b)
    # print('\n\n')
    elif(operator == "/"):
        div(a,b)
    elif(operator == "*"):
        mult(a,b)
    elif(operator == "-"):
        subt(a,b)
    else:
        print('invalid operator: ')


def add(a,b):    
    print('\n\n')
    sum = float(a+b)
    print ('sum: ', sum)
    return sum
 
# add(a1,b1)

def subt(a,b): 
    subt = float(a-b)
    print ('subtraction: ', subt)
    return subt
 
# subt(a1,b1)

def mult(a,b): 
    mult = float(a*b)
    print ('multiplication: ', mult)
    return mult
 
# subt(a1,b1)

def div(a,b):
    div= float(a/b)
    print ('division: ', div)
    return div
 
# div(a1,b1)

calculator(a1,b1)


