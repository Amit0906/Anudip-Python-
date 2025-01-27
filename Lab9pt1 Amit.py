"""Write a Python program that prompts the user to input an integer and raises a
ValueError exception if the input is not a valid integer.
"""
#defining a function to check input
def input_check():
    while True: 
        try :
            value=int(input("Input an integer ")) #telling user to enter an integer
            return value                          #if its an integer, returns and allocates the integer to the variable 'number' in line 13
        except ValueError:                        #else if its not an integer, it prints the error message and reruns the line 8
            print("Invalid Input. It should be an Integer")

number=input_check()                              #calling the function
print(f"Your value is {number}")                  #if its an integer, it prints the message