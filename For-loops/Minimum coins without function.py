"""You have three types of coins , values of 1, 3 and 5
given a number, you need to find minimum coins required. 
eg., if input is 8 - answers 5(1), 3(1) - 2 coins 
if input is 10 - answer is 5(2) - 2 coins
if input is 4 - answer is 3(1), 1(1) - 2 coins
if input is 17 - answers is 5(3), 1(2) - 5 coins
"""

coins = [5, 3, 1]   #A list of 3 integers(coins)
length=len(coins)   #Finds the length of coins list
coin_counts = [0, 0, 0]  # Number of 5-coins, 3-coins, and 1-coins respectively
number=int(input('Enter any number')) #Get any number from the user
Input_number=number

for i in range(length):
    while number >= coins[i]:   #ex: suppose number=6: while 6>=5  => True
        number-= coins[i]       #    Now number = 6-5 = 1
        coin_counts[i] += 1     #    coin_counts[0] is incremented by 1 ,This continues until the while loop condition becomes false

min_coins = sum(coin_counts)  #Adds the values in coin_counts list; suppose coin_counts=[1,0,3] then total_coins=1+0+3=4

#output
print(f"Input: {Input_number} - Answer: Minimum number of coins - {min_coins} coins")
print(f'5-coins:{coin_counts[0]},3-coins:{coin_counts[1]},1-coins:{coin_counts[2]}')
