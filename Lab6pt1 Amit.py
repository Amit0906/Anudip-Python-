"""Write a Python program to Count all letters, digits, and special
symbols from the given string"""

chars=0     #initializing chars to 0
digits=0    #initializing digits to 0
symbol=0    #initializing symbol to 0
#When taking input from user
#sentence=input("Enter a string: ")

#pre given input
sentence="P@#yn26at^&i5ve"
for i in sentence:
    if i.isalpha():
        chars+=1    #P,y,n,a,t,i,v,e
    elif i.isdigit():
        digits+=1   #2,6,5
    else:
        symbol+=1   #@,#,^,&

print(f"Chars = {chars}, Digits = {digits}, Symbol = {symbol}")