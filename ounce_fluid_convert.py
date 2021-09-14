

#a program to convert cups to fluid ounce

def cup_shop():
    
    intro()
    #cup is an arguement.................
    cup = int(input('enter the number of cups: '))
    cups_entry(cup)
    

def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces. For your')
    print('reference the formula is:')
    print(' 1 cup = 8 fluid ounces')
    print()

def cups_entry(cup):
    # cup = 800   changing parameter vairble
    ounce_fluid = 1/8  
    Amount = int(cup/ounce_fluid)
    print(' you supply', cup ,'cups: ')
    print(' You have: ', Amount, 'ounce fluid')
    return Amount



cup_shop()