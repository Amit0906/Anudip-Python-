"""Write a Python Count vowels in a string"""

sentence="Welcome to Python Assignment"
count=0 #initializing count to 0

for s in sentence:
    if s=='a' or s=='e' or s=='i' or s=='o' or s=='u' or s=='A' or s=='E' or s=='I' or s=='O' or s=='U':
        count+=1

print(f"Total no. Vowels are = {count}")