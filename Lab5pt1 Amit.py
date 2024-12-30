"""Declare a div() function with two parameters. Then call the function and pass two numbers and display their division."""

#defining a function to divide two numbers
def div(x,y):
    return x/y

x=int(input("Enter the First Number: "))#taking input of the first number
y=int(input("Enter the Second Number: "))#taking input of the second number

print(f"Divison between {x} & {y} gives the result {div(x,y)}")