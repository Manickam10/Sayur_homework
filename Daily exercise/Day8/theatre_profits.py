"""
Write a program that calculates the profit generated by a movie theatre for different ticket classes.

For VIP tickets, the profit is 30% of the ticket price + Rs120 for every ticket sold.
For General tickets, the profit is 20% of the ticket price + Rs80 for every ticket sold.
For Matinee show tickets, the profit is a flat 15% of the ticket price.
Input: Ticket price and number of tickets sold for each ticket class.
Output: Calculate and print the total revenue generated by the theatre in a day.
"""
def calculate_profit(ticket_price,tickets_sold,percentage,fixed_amount):
    profit = tickets_sold*((percentage/100)*ticket_price + fixed_amount)
    return profit

#Assuming there are three shows running in the theatre daily:Morning,matinee,evening
# Get input from the user
VIP_tickets_price = float(input("Enter the price for VIP tickets: "))
General_tickets_price = float(input("Enter the price for General tickets: "))

VIP_tickets_sold_mor = int(input("Enter the number of VIP tickets sold in Morning show: "))
General_tickets_sold_mor = int(input("Enter the number of General tickets sold in Morning show: "))

VIP_tickets_sold_eve = int(input("Enter the number of VIP tickets sold in Evening show: "))
General_tickets_sold_eve = int(input("Enter the number of General tickets sold in Evening show: "))

matinee_show_price = float(input("Enter the price for matinee show tickets: "))
matinee_tickets_sold = int(input("Enter the number of matinee show tickets sold: "))


# Calculate profit for each class
VIP_tickets_profit_mor = calculate_profit(VIP_tickets_price, VIP_tickets_sold_mor, percentage=30, fixed_amount=120)
General_tickets_profit_mor = calculate_profit(General_tickets_price, General_tickets_sold_mor, percentage=20, fixed_amount=80)
Morning_show_profit = VIP_tickets_profit_mor + General_tickets_profit_mor

Matinee_show_profit = calculate_profit(matinee_show_price,matinee_tickets_sold,percentage=15,fixed_amount=0)

VIP_tickets_profit_eve = calculate_profit(VIP_tickets_price, VIP_tickets_sold_eve, percentage=30, fixed_amount=120)
General_tickets_profit_eve = calculate_profit(General_tickets_price, General_tickets_sold_eve, percentage=20, fixed_amount=80)
Evening_show_profit = VIP_tickets_profit_eve + General_tickets_profit_eve

# Calculate total profit
total_Revenue = Morning_show_profit + Matinee_show_profit + Evening_show_profit

# Display the results
print(f"Profit for Morning show: Rs: {Morning_show_profit}")
print(f"Profit for Matinee show: Rs: {Matinee_show_profit}")
print(f"Profit for Evening show: Rs: {Evening_show_profit}")
print(f"Total Revenue in a day: Rs: {total_Revenue}")