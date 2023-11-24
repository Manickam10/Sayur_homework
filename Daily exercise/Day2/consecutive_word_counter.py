""" Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words 
that are the same without any other specific word in between.
 For example, count the occurrences of "apple apple" but not "apple orange apple." """

passage = input("Enter any passage or string: ")

words=passage.split(" ") #splits the passage into words separated by spaces in a list

occurences = 0 #variable to count the occurences of any two consecutive words
for word in range(len(words)-1): 
    if words[word] == words[word+1]:  #checking if the current word and next word are same
        occurences += 1

print(f"occurences of two consecutive words:{occurences}")