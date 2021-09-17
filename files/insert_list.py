

# This program demonstrates the insert method.

def main_insert():
 # Create a list with some names.
    names = ['James', 'Kathryn', 'Bill', 'Aisha']
 
 # Display the list.
    print('The list before the insert:')
    print(names)
 
 # Insert a new name at element 0.
    names.insert(4, 'Joe')
 
 # Display the list again.
    print('The list after the insert:')
    print(names)

# Call the main function.
main_insert()