
# This program reads a file's contents into a list.

def main():
# Open a file for reading.

    input_file = open('cities.txt', 'r')

    # Read the contents of the file into a list.
    cities = input_file.readlines()

    # Close the file.
    input_file.close()
    # Strip the \n from each element.
    index = 0
    while index < len(cities):
            cities[index] = cities[index].rstrip('\n')
            index += 1

    # Print the contents of the list.
    print(cities)

#closing the main function
main()