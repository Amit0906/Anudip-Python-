#Write a program to input 3 sides of a triangle
#and calculate and print its area.
#importing math 
import math

#taking user input
a=int(input("Enter the first side of the triangle :"))
b=int(input("Enter the second side of the triangle :"))
c=int(input("Enter the third side of the triangle :"))

#finding Semi perimeter
semi_primeter=(a+b+c)/2
area=math.sqrt(semi_primeter*(semi_primeter-a)*(semi_primeter-b)*(semi_primeter-c))

print("The Area of the triangle is :",area)