
# This program reads numbers from a file into a list.

def main():
# Open a file for reading.
    input_file = open('numberlist.txt', 'r')
 
 # Read the contents of the file into a list.
    numbers = input_file.readlines()
 
  # Close the file.
    input_file.close()
 
 # Convert each element to an int.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1
 
  # Print the contents of the list.
    print(numbers)

# Call the main function.
main()