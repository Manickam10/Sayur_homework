"""7.2Program to find out how many Kg of onion or tomato we can buy.The price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34.
.And add 3% of the budget for petrol expenses.""" 

#Function to calculate the quantity of onion or tomato we can buy
def Calculate_items_budget_2(Budget,city,tomato_price):
    Chennai_onion_price=30  #price of one kg of onion in chennai
    Trichy_onion_price=27   #price of one kg of onion in Trichy
    Madurai_onion_price=34  #price of one kg of onion in Madurai
    petrol_expenses=0.03*Budget # 3% of the budget for petrol expenses
    New_Budget=Budget-petrol_expenses  #New Budget=Budget-petrol expenses
    
    if city=='CHENNAI':
        Max_onion_kg=New_Budget//Chennai_onion_price
        Max_tomato_kg=New_Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg
    elif city=='TRICHY':
        Max_onion_kg=New_Budget//Trichy_onion_price
        Max_tomato_kg=New_Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg
    elif city=='MADURAI':
        Max_onion_kg=New_Budget//Madurai_onion_price
        Max_tomato_kg=New_Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg
    else:
        Default_onion_price=20
        Max_onion_kg=New_Budget//Default_onion_price
        Max_tomato_kg=New_Budget//tomato_price
        return Max_onion_kg,Max_tomato_kg



#Tomato price is constant
Tomato_price=10.5

#Get the budget from the user
Budget=float(input('Enter the budget amount in Rs.'))

#Get the city where the user is going for shopping
City=input("Enter the city you are going to buy onion or tomato (Chennai,Trichy,Madurai) ")
CITY=City.upper()
#pass the budget,city and tomato price to function
onion_quantity,tomato_quantity=Calculate_items_budget_2(Budget,CITY,Tomato_price)

#output
print(f'With Rs.{Budget} including 3% for petrol expenses in {City}, You can buy: ')
print(f"{onion_quantity:} Kg of onion")
print(f"{tomato_quantity:} Kg of tomato")
