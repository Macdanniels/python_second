# This program saves a list of numbers to a file.

def main():
# Create a list of numbers.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

 # Open a file for writing.
    output_file = open('numberlist.txt', 'w')

 # Write the list to the file.
    for item in numbers:
        output_file.write(str(item) + '\n')

 # Close the file.
    output_file.close()

# Call the main function.
main()