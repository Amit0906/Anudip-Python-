#Python Program to Find the Largest Among Three Numbers (Using nested if)

#Input 3 numbers from user
num1=(int(input("Enter the First number: ")))
num2=(int(input("Enter the Second number: ")))
num3=(int(input("Enter the Third number: ")))

if num1>num2:
    if num1>num3:
        max=num1
    else:
        max=num3
else:
    if num2>num3:
        max=num2
    else:
        max=num3

#Print the largest number
print(f"{max} is the largest among three")