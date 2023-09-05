"""The user just bought a few things in your  shop. Ask the user what he bought.
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input).
Print the change amount you have to give to the user.
Hint - use float datatype"""

#Function to find total cost
def total_cost(vadai,soda,sandwich):
    vadai_cost=30  #Cost of one vadai
    soda_cost=20   #Cost of one soda
    sandwich_cost=100 #Cost of one sandwich
    total = vadai * vadai_cost + soda * soda_cost + sandwich * sandwich_cost
    return total


#Ask the customer what he bought
print("Welcome to our shop")
vadai=int(input('Enter the number of vadais bought '))
soda=int(input('Enter the number of sodas bought '))
sandwich=int(input('Enter the number of sandwiches bought '))
total=total_cost(vadai,soda,sandwich)
print("Total cost for the items you bought is Rs.",total)

#Get the input of amount paid by the customer
amount_paid=float(input('Enter the amount paid by the customer'))

#Calculation of change amount
change_amount= amount_paid-total
if change_amount>=0:
    print("Change amount to give is Rs.",change_amount)
else:
    print("The amount paid is not enough")