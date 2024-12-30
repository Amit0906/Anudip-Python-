"""Using max() and min() functions display the maximum and minimum of 5 random
    numbers."""

#input 5 numbers from user
print("Enter 5 numbers")
a=int(input("First Number: "))
b=int(input("Second Number: "))
c=int(input("Third Number: "))
d=int(input("Fourth Number: "))
e=int(input("Fifth Number: "))

#printing Max and min element from the input numbers
print(f"{max(a,b,c,d,e)} is the largest and {min(a,b,c,d,e)} is the smallest element among the numbers {a}, {b}, {c}, {d}, {e}")
