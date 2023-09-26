"""
2. Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 
"""

import re

Username = input("Enter your username: ")
password = input("Enter password: ")

if ( re.search(r'[a-zA-Z]',Username) and re.search(r'@',Username) and re.search(r'\.(com|org|tech|edu)$',Username) ):
    if (re.match(r'.+@+.+\.(com|org|tech|edu)$',Username)):
        print('Username is correct')
        company_name = Username.split('@')[1].split('.')[0]
        extract_username = Username.split('@')[0]
        expected_password = extract_username[0] + extract_username[2] + extract_username[-3:] + company_name[:3]
        if re.match(r'[0-9]{3}$',password):
               if re.match(expected_password,password):
                   print("Username and password is correct")
                   print(f"Username: {Username}\nPassword: {password}")
               else:
                    print("Invalid password")
        else:
             print("Username is correct but password is invalid")
    else:
         print("Username is incorrect")

         
             
    
