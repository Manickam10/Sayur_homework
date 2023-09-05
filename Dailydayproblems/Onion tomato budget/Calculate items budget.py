"""Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget. """

#Function to Find the quantity of onion or tomato we can buy
def Calculate_budget(Budget):
    Onion_price=20   #Price of One kg of Onion in Rs
    Tomato_price=10.5 #Price of One kg of Tomato in Rs
    Max_onion_kg=Budget//Onion_price
    Max_tomato_kg=Budget//Tomato_price
    return Max_onion_kg,Max_tomato_kg

#Get the budget from the user
Budget=float(input("Enter the budget amount in Rs:" ))
#Pass the budget to function to calculate the qunaity of onions or tomatos
onion_kg,Tomato_kg=Calculate_budget(Budget)
#output
print(f"With {Budget} Rs, you can buy:")
print(f"{onion_kg} kg of onion")
print(f"{Tomato_kg} kg of tomato")
