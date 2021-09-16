
# This program writes three lines of data
  # to a file.
def main():
 # Open a file named philosophers.txt.
    
    outfile = open(r'philosophers.txt', 'w')
 
  # Write the names of three philosphers
  # to the file.
    outfile.write('John Locke\n')             #writing to the line...
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    # outfile.write('De Rock\n')

    print("names inserted")
 
  # Close the file
    outfile.close()
 
 # Call the main function.
main()