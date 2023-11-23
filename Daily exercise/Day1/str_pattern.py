"""
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row"""
# current_letter = 'a'
# output = ''

# for _ in range(5):  # Loop for 5 rows
#     output += current_letter  # Add the current letter
#     print(output)
#     previous_letter = output
#     current_letter = chr(ord(current_letter) + 1)  # Increment to the next letter in the alphabet
#     output = output + current_letter
#     output += previous_letter
#     print(output)
    
output = ''
#ascii value of 'a'=97,ascii value of 'g'=103
for current_letter in range(97,104):
    output = output + chr(current_letter) + output
    print(output)

"""output:
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba

"""    