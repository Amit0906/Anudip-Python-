"""Write a Python program to remove duplicate characters of a given
string."""

#Given sentence
sentence="String and String Function"

listed_sentence=sentence.split()        #converting sentence to a list
unique_words=[]                         #initializing unique_words list

for word in listed_sentence:
    if word not in unique_words:
        unique_words.append(word)       #adding new words to the list

new_sentence = " ".join(unique_words)   #converting list to a sentence

print(new_sentence)                     #printing the sentence with no duplicates