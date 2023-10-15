"""
Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd"""


# Input encrypted string
encrypted_string = input("Enter the encrypted string: ")

# Initialize variables to store the decrypted string and its length
decrypted_string = ""
length = 0

# Initialize a variable to keep track of the current character
current_char = 1

# Iterate through each character in the input string
for char in encrypted_string:
    # If the character is a digit, update the current character
    if char.isdigit():
        current_char = int(char)
        decrypted_string += decrypted_string * current_char
    # If the character is an alphabet, add it to the decrypted string the specified number of times
    elif char.isalpha():
        decrypted_string +=  char * current_char 
        length += current_char
    # If the character is a special character, ignore it
    else:
        continue

# Print the decrypted string and its length
print("Decrypted string:", decrypted_string)
print("Length:", length)

"""
Expected output:
ac2bd3
"""