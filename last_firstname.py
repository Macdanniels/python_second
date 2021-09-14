

def get_name():
# Get the user's first and last names.
    first = input('Enter your first name: ').title()
    last = input('Enter your last name: ').title()
# Return both names.
    print('NAME: ', first, last)
    return first, last


first_name, last_name = get_name()


# def do_something(number):
#     return number * 2

# print(do_something(10))