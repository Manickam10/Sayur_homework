"""
1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.
"""


import re

password=input("Enter your password: ")
# Check if the password is at least 8 characters long
if len(password) < 8:
    print("Please enter a password above 8 characters")
    exit(0)
    
# Check if the password contains at least one alphabet, one number, and one special character
if (   re.search(r'[a-zA-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*()-_+=]', password)):
    # Check if the password meets the strong or very strong criteria

    if (  len(re.findall(r'[a-zA-Z]', password)) >= 3 and len(re.findall(r'\d', password)) >= 2 and len(password) >= 16):
        strength = "Very strong"
        Acceptable = "Yes"
    elif( len(re.findall(r'[a-zA-Z]', password)) >= 3 and 
           len(re.findall(r'\d', password)) >= 2
        ):         
        strength = "strong"
        Acceptable = "Yes"
    else:
        strength = "ok"
        Acceptable = "Yes"
# If the password doesn't meet the above criteria, it's considered weak
else:
    strength = "weak"
    Acceptable = "No"

print(f"Password: {password}\nStrength: {strength}\nAcceptable: {Acceptable}")

