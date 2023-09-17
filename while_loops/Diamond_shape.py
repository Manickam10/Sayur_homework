######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

max_line = int(input("Enter the maximum number of lines (up to 10): "))
current_line=1

#printing first half of diamond shape
while current_line <= max_line:
    spaces = " " * (max_line - current_line) #creating spaces
    diamonds = "$ " * (current_line)  #creating diamonds characters
    print(f"{spaces} {diamonds}")     #printing for eg. say first row of diamond
    user_input =input("")             #After printing each line, wait for user input.   
    current_line += 1                 #Increment current line by 1
    if user_input == " ":             #If the user presses space, continue
        continue
    else:                             #If the users presses any other key, stop printing
        break

#printing remaining half of diamond shape
current_line = max_line - 1
while current_line <= max_line:
    spaces = " " * (max_line - current_line)
    diamonds = "$ " * (current_line)
    print(f"{spaces} {diamonds}")
    user_input =input("")
    current_line -= 1
    if user_input == " ":
        continue
    else:
        break

 #output:
 # Enter the maximum number of lines (up to 10): 4
 #   $ 
 
 #  $ $ 
 
 # $ $ $ 
 
 #$ $ $ $ 
 
 # $ $ $ 
 
 #  $ $ 
 
 #   $   

    
    

