"""Write a function in Python to count and display the total number of words in a text
file “ABC.txt”"""

#writng in the text file ABC.txt
with open("ABC.txt","w") as fileobj:
    fileobj.write("To change the overall look of your document.\n")
    fileobj.write("To change the look available in the gallery")

#reading file
with open("ABC.txt","r") as file:
    list_of_all_lines=[]                    #initializing a list
    line=file.readline()                    #reading the first line

    while line:
        line_list=line.split()              #converting current line to a list
        list_of_all_lines.extend(line_list) #adding current list to a bigger list containg all lines
        line=file.readline()                #reading the next line

    count=0                                 #initializing count to 0
    for words in list_of_all_lines:
        count+=1                            #counting the number of elements(words) in the LIST list_of_all_lines

    print(f"The total number of words in text file ABC.txt is {count}")
