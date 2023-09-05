"""7.1 Program to find out how many Kg of onion or tomato we can buy. but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. 
Input is budget and city."""

#Function to calculate the quantity of onion or tomato we can buy
def Calculate_items_budget_2(Budget,city,tomato_price):
    Chennai_onion_price=30  #price of one kg of onion in chennai
    Trichy_onion_price=27   #price of one kg of onion in Trichy
    Madurai_onion_price=34  #price of one kg of onion in Madurai
    if city=='Chennai'or'chennai':
        Max_onion_kg=Budget//Chennai_onion_price
        Max_tomato_kg=Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg
    elif city=='Trichy'or'trichy':
        Max_onion_kg=Budget//Trichy_onion_price
        Max_tomato_kg=Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg
    elif city=='Madurai'or'madurai':
        Max_onion_kg=Budget//Madurai_onion_price
        Max_tomato_kg=Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg
    else:
        Default_onion_price=20
        Max_onion_kg=Budget//Default_onion_price
        Max_tomato_kg=Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg



#Tomato price is constant
Tomato_price=10.5
#Get the budget from the user
Budget=float(input('Enter the budget amount in Rs.'))
#Get the city where the user is going for shopping
City=input("Enter the city you are going to buy onion and tomato ")
#pass the budget,city and tomato price to function
onion_quantity,tomato_quantity=Calculate_items_budget_2(Budget,City,Tomato_price)
#output
print(f'With Rs.{Budget} in {City}, You can buy: ')
print(f"{onion_quantity:} Kg of onion")
print(f"{tomato_quantity:} Kg of tomato")
