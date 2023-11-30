"""
Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A. 
Player who gets 5 points first wins the game.
Print the board each time after the user rolls and also print the current score.
Use functions
"""

import random

#Function to print the board      
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

#Function to roll the dice
def roll_dice():
    return random.randint(1,6)

if __name__ =="__main__":
    #Initializing or creating board
    board=[]
    for i in range(6):
        col_board=[]
        for j in range(6):
            col_board.append('*')   
        board.append(col_board)
    
    player_A_score = 0
    player_B_score = 0

    while player_A_score < 5 and player_B_score < 5:
        
        #Player A's turn
        user_input_a = input("Player A, Enter roll(r)...")
        if user_input_a.lower() == 'r':
            row_A = roll_dice()-1
            col_A= roll_dice()-1
            if board[row_A][col_A] == 'B':
                player_A_score += 1
                board[row_A][col_A] = 'A'
                print_board(board) 
                print(f"Score:A-{player_A_score},Score:B-{player_B_score}")
            else:
                board[row_A][col_A] = 'A'
                print_board(board) 
                print(f"Score:A - {player_A_score},Score:B - {player_B_score}")

            if player_A_score >= 5:
                print("Player A wins!")
                break
        else:
            print('player A quits the game')
            break
            
        
        #Player B's turn
        user_input_b = input("Player B, Enter roll(r)...")
        if user_input_b.lower() == 'r':
            row_B = roll_dice() - 1
            col_B = roll_dice() - 1

            if board[row_B][col_B] == 'A':
                player_B_score += 1
                board[row_B][col_B] = 'B'
                print_board(board)
                print(f"Score: A - {player_A_score}, B - {player_B_score}")
            else:
                board[row_B][col_B] = 'B'
                print_board(board)
                print(f"Score: A - {player_A_score}, B - {player_B_score}")


            if player_B_score >= 5:
                print("Player B wins!")
                break
        else:
            print('player B quits the game')
            break

#output
# Player A, Enter roll(r)...r
# * A * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

# Score:A - 0,Score:B - 0   
# Player B, Enter roll(r)...r
# * A * * * *
# * * * * * *
# B * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

# Score: A - 0, B - 0
# Player A, Enter roll(r)...r
# * A * * * *
# * * * * * *
# B * * * * *
# * * * * * *
# * A * * * *
# * * * * * *

# Score:A - 0,Score:B - 0
# Player B, Enter roll(r)...r
# * A * * * *
# * * * * * *
# B * * * * *
# B * * * * *
# * A * * * *
# * * * * * *

# Score: A - 0, B - 0
# Player A, Enter roll(r)...