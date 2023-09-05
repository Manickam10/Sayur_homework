"""Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per
 person is half of lunch cost. Cost of the hall is Rs 200 per person.
  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. 
  Decide what should be the input and calculate the cost.
  The total cost is split equally by bride and groom.
 Bride has saved Rs50000. Determine if the bride has to take a loan or not. 
 If loan, how much?"""

Cost_of_lunch=200  #Cost for lunch per person is Rs200
Cost_of_breakfast=Cost_of_lunch/2 #Cost for Breakfast per person is half of lunch cost
Cost_of_hall=200 #Cost of the hall is Rs 200 per person
Cost_of_decoration=Cost_of_hall/2 #Decoration is 50% of Hall cost
Parking=0.1*Cost_of_hall #Parking is 10% of the Hall cost

#Get the user input how many number of guests are attending the wedding
No_of_persons=int(input('Enter how many number of persons attending the wedding '))

#Calculation of total wedding cost
Total_lunch_cost = Cost_of_lunch * No_of_persons
Total_breakfast_cost = Cost_of_breakfast * No_of_persons
Total_hall_cost = Cost_of_hall * No_of_persons
Total_decoration_cost = Cost_of_decoration * No_of_persons
Total_parking_cost = Parking * No_of_persons
Total_wedding_cost = Total_breakfast_cost + Total_decoration_cost + Total_hall_cost + Total_lunch_cost + Total_parking_cost

print(f'The total wedding expenses will be {Total_wedding_cost} by the number of guests attending the wedding')

#The total cost is split equally by bride and groom
Wedding_cost_for_Bride,Wedding_cost_for_Groom=Total_wedding_cost/2,Total_wedding_cost/2

#Bride has saved Rs50000
Bride_savings=50000

#TO check whether the bride has to take a loan or not
if Wedding_cost_for_Bride<=Bride_savings:
    print("The Bride don't want to take loan")
else:
    loan=Wedding_cost_for_Bride-Bride_savings
    print("The bride has to take a loan of Rs.",loan)
