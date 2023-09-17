########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

input_string=input("Enter any sentence: ")
#Converting string in to list
string = input_string.split()  
print(string)
#Iterating each word in string 
for word in string:
    first_letter = word[0]
    rest_word = word[1:]
    final_word = rest_word + first_letter +'ay'
    print(f"{final_word} ",end="")