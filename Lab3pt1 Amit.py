#1. Using input() function take one number from the user and using ternary operators
#check whether the number is even or odd
number=int(input("Enter a number: "))
result="Even" if number%2==0 else "Odd"
print("The number is",result)