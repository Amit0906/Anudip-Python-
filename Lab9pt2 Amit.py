"""Write a Python program that opens a file and handles a FileNotFoundError exception
if the file does not exist"""

try:
    with open("DLF.txt","r") as file:   #opening a file DLF.txt in read mode
        line=file.readline()            #reading first line of the file
except FileNotFoundError:               #if the file does not exist, shows an error message
    print("File does not exist")