"""Write a Python program to count Uppercase, Lowercase, special
character and numeric values in a given string"""

digits=0    #initializing digits to 0
symbol=0    #initializing symbol to 0
upper_case=0#initializing upper_case to 0
lower_case=0#initializing lower_case to 0

sentence="Hell0 W0rld ! 123 * # welcome to pYtHoN"
for i in sentence:
    if i.isdigit():
        digits+=1       #0,0,1,2,3
    elif i.isupper():
        upper_case+=1   #H,W,Y,H,N
    elif i.islower():
        lower_case+=1   #e,l,l,r,l,d,w,e,l,c,o,m,e,p,t,o
    else:
        symbol+=1       #!,*,#,' '

print(f"Uppercase = {upper_case}, Lowercase = {lower_case}, Specialcase = {symbol}, Numeric = {digits}")
