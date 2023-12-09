"""
Problem #1.
Write a program for calculating the profit for railways.
For first class tickets, the profit is 25% of the price + Rs100 for every ticket sold.
For Second class tickets, the profit is 15% of the price + Rs70 for every ticket sold.
For Third class tickets (i don't know if there is a third class), the profit is 5% of the price.

Get the price and no of tickets sold for each class and calculate the total profit. 
Identity what calculation in the above problem can be written as a function 
and what the input and output should be.
"""
#input - price and no of tickets for each class
#output - profit

# def profit_calculation(price,no_of_tickets):
#     total_profit = 0
#     for i in range(len(price)):
#         if i+1 == 1:
#             total_profit += no_of_tickets[i]*(0.25*price[i]+100)
#         if i+1 == 2:
#             total_profit += no_of_tickets[i]*(0.15*price[i]+70)
#         if i+1 == 3:
#             total_profit += no_of_tickets[i]*(0.05*price[i])
#     return total_profit



# price_of_each_class=[]
# no_of_tickets_in_each_class=[]
# for i in range(3):
#     print(f"Enter the details of {i+1} class tickets: ")
#     price=int(input("Enter the price of each ticket: "))
#     price_of_each_class.append(price)
#     num = int(input("Enter the number of tickets sold in each class: "))
#     no_of_tickets_in_each_class.append(num)
# print(f"Total profit = Rs.{profit_calculation(price_of_each_class,no_of_tickets_in_each_class)}")


def calculate_profit(price,no_tickets_sold, percentage, fixed_amount=0):
    profit = (price * percentage / 100) * no_tickets_sold + (fixed_amount * no_tickets_sold)
    return profit

# Get input from the user
first_class_price = float(input("Enter the price for first class tickets: "))
first_class_tickets_sold = int(input("Enter the number of first class tickets sold: "))

second_class_price = float(input("Enter the price for second class tickets: "))
second_class_tickets_sold = int(input("Enter the number of second class tickets sold: "))

third_class_price = float(input("Enter the price for third class tickets: "))
third_class_tickets_sold = int(input("Enter the number of third class tickets sold: "))

# Calculate profit for each class
first_class_profit = calculate_profit(first_class_price, first_class_tickets_sold, percentage=25, fixed_amount=100)
second_class_profit = calculate_profit(second_class_price, second_class_tickets_sold, percentage=15, fixed_amount=70)
third_class_profit = calculate_profit(third_class_price, third_class_tickets_sold, percentage=5)

# Calculate total profit
total_profit = first_class_profit + second_class_profit + third_class_profit

# Display the results
print(f"Profit for First Class: Rs{first_class_profit}")
print(f"Profit for Second Class: Rs{second_class_profit}")
print(f"Profit for Third Class: Rs{third_class_profit}")
print(f"Total Profit: Rs{total_profit}")
