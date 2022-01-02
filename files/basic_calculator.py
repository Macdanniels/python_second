
def main():
    
    print("BASIC SIMPLE CALCULATOR")
    num1 = calculator()
    
def calculator():
    again = "yes"
  
    while again == "yes":
        
        try:
            num1 = float(input("Enter first Number: "))
        except ValueError:
            print("enter a valid entry")
            num1 = float(input("Enter first Number: "))
        operator = input("Enter operator symbol:  ")
        try:
            num2= float(input("Enter second Number : "))
        except ValueError:
            print("enter a valid number")
            num2 = float(input("Enter second Number: "))
        if operator == "+":
            
            print(num1 + num2)
            print(" Do you want to perform another operations?")
            again = input('Enter your decision:')
            
            #     print('Calculation Operation')
        elif operator == "*":
                
                print(num1* num2)
                print(" Do you want to perform another operations?")
                again = input('Enter your decision:')
                
        elif operator == "-":
                
                print(num1- num2)
                print(" Do you want to perform another operations?")
                again = input('Enter your decision:')

        elif operator == "/":
                print(num1 / num2)
                print(" Do you want to perform another operations?")
                
        else:
            a = str(input("your name: "))
            print (a + " you entered an invalid operator ")
            print(" Do you want to perform another operations?")
            again = input('Enter your decision:')            

main()	
        