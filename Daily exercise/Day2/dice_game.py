"""
Problem #3
Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
added. If the number is odd, then if the number is 1,3 then the user has to jump. 
If the number is 5, then 3 points are added. The game ends when the user has 50 points
"""
import random

points=0
while points<=50:
    user_input=input(print("Roll or quit (r or q): "))
    
    if user_input == 'r':
        roll_the_dice=random.randint(0,6)
        
        if roll_the_dice == 0:
            print("Game over. You rolled a 0.")
            break
        elif roll_the_dice % 2 == 0:
            points+=2
            print(f"Rolled {roll_the_dice}. You got 2 points. Total points: {points}")
        elif roll_the_dice in [1,3]:
            print(f"Rolled {roll_the_dice}. You have to jump!")
            continue
        else:
            points+=3
            print(f"Rolled {roll_the_dice}. You got 3 points. Total points: {points}")            
    
    elif user_input =='q':
        break
    
    else:
        print("Enter Roll or quit (r or q)!!!")
        continue

if points>= 50:
    print(f"Congratulations! You reached {points} points and won the game.")
else:
    print("Game over")
        
