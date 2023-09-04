def find_minimum_coins(amount):
    coins = [5, 3, 1]   #A list of 3 integers 
    length=len(coins)   #Finds the length of coins list
    coin_counts = [0, 0, 0]  # Number of 5-coins, 3-coins, and 1-coins respectively

    for i in range(length):
        while amount >= coins[i]:   #ex: suppose amount=6: while 6>=5  => True
            amount-= coins[i]       #    Now amount = 6-5 = 1
            coin_counts[i] += 1     #    coin_counts[0] is incremented by 1 ,This continues until the while loop condition becomes false

    total_coins = sum(coin_counts)  #Adds the values in coin_counts list; suppose coin_counts=[1,0,3] then total_coins=1+0+3=4
    return coin_counts, total_coins



#Get any number from the user
number=int(input('Enter any number'))

#To pass the number to the function to find the minimum coins and count of each coins(1,3,5)
coin_counts, min_coins = find_minimum_coins(number)

#output
print(f"Input: {number} - Answer: Minimum number of coins - {min_coins} coins")
print(f'5-coins:{coin_counts[0]},3-coins:{coin_counts[1]},1-coins:{coin_counts[2]}')
