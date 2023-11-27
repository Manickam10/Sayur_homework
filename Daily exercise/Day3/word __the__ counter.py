"""
Problem #2
Read a passage from a file. 
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

answer is 4 (The king, the forest, The King the next).
"""
first_the='the'
middle_word='a'
first_the_next_the=[]
count_the=[]
try:
    with open('Daily exercise\Day3\File1.txt','r') as file:
        passage = file.read()
            
        # Split the passage into words
        words = passage.lower().split()
            
        # Initialize count
        count = 0
            
        # Iterate through words to count occurrences
        for word in range(0,len(words)-1):
            if words[word] == first_the :
                first_the_next_the.append(words[word])
                for next_word in range(word+1,len(words)):
                    first_the_next_the.append(words[next_word])
                    if words[next_word] == first_the:
                        if middle_word not in first_the_next_the:
                            count+=1
                            count_the.extend(first_the_next_the[0:2])
                        first_the_next_the.clear()
                        break
        print(f"count:{count}({count_the})")
                                  
except FileNotFoundError:
    print(f"Error: File does not exist.")



