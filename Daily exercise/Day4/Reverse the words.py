"""
Problem #1
write a program that reads a passage and reverses the order of 
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
Output I ma ruyaS
"""
#Function to reverse each word from the passage 
def reverse_words(passage):
    reversed_words=[]
    words = passage.split()
    for word in words:
        reversed_word = word[::-1] #reverse the word
        reversed_words.append(reversed_word)
    return reversed_words


Passage = input('Enter any passage:' )
Output_passage = ' '.join(reverse_words(Passage))
print(Output_passage)

#output
# Enter any passage:i am sayur
# i ma ruyas