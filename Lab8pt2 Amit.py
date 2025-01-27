"""Write a function display_words() in python to read lines from a text file "story.txt",
and display those words, which are less than 4 characters."""

#writng in the text file story.txt
with open("story.txt","w") as fileobj:
    fileobj.write("To change the overall look of your document.\n")
    fileobj.write("To change the look available in the gallery")

#reading from the txt file story.txt
with open("story.txt","r") as file:
    line=file.readline() #Storing first line in line
    while line:
        line_list=line.split()  #converting the string into a text
        display_words=[]        #initializing a list 
        for words in line_list: #checking each element from list
            if len(words) < 4:
                display_words.append(words) #adding words that are less than length of 4 to the list display_words

        arrange_words=" ".join(display_words) #converting the list to a string with only the words that have less than 4 characters
        print(arrange_words) #printing the string
        line=file.readline() #reading next line

    
    # counting length of each element
    """def display_words(string):
        return len(string)
    count_words=[display_words(element) for element in line_list]
    print(count_words)"""