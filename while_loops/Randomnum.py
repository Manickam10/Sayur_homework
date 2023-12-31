######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import random

computer_integer = random.randint(1,100)
attempt = 0
while(True):
    guess = int(input("Enter your guessed number: "))
    if computer_integer < guess :
        print("High")
    elif computer_integer > guess :
        print("Low")
    else:
        break
    attempt+=1

print("You guessed the number correctly")
print ("User guessed the number in ", attempt, "attempts")

#output
"""
Enter your guessed number: 34
Low
Enter your guessed number: 56
High
Enter your guessed number: 40
Low
Enter your guessed number: 46
Low
Enter your guessed number: 49
Low
Enter your guessed number: 50
Low
Enter your guessed number: 55
High
Enter your guessed number: 53
You guessed the number correctly
User guessed the number in  7 attempts
"""
