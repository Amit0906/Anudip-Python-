""" A transport company charges the fare according to following table:
    Distance    Charges
    1-50 	    8 Rs./Km
    51-100 	    10 Rs./Km
    >100 	    12 Rs/Km

    Q) Write a program to input distance travelled as input and calculate and print the total charge.
       Use comments where necessary and follow python naming conventions.
"""
#Take distance as input
distance=(int(input("Enter the Distance you have travelled: ")))

if distance<=50 :
    charge=distance*8
elif distance<=100 :
    charge=distance*10
else:
    charge=distance*12

#Print the distance as well as charge
print(f"For {distance}km of distance, you need to pay Rs{charge} as charge.")