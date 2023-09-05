############## Problem  3  #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
# initialise all the variables needed
Basic_pay=10000
previousMonthSalary=0
cumulativeMonthSalary=0
for month, phoneCount in enumerate(monthlySalesList):
    #calculate the Salary using If stmts
    
    print("\n")
    print(f"Salary for {month+1} month :")
    if phoneCount >= 5:
       currentMonthSalary = Basic_pay + (phoneCount - 5)*1100 + 5000 #For every 5 phones sold, Rs 5000 bonus.#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
    else:
        currentMonthSalary = Basic_pay
       
    print (f"This month's salary before additional bonus {currentMonthSalary}") 

    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.

    if(phoneCount < 20):
        previousMonthSalary = currentMonthSalary #we set this so that, we can use this info in the next iteration
        #no need to calculate anything because <20 phones sold
    else:
        if previousMonthSalary > 20000:
            #calculate the new salary
            currentMonthSalary += 5000
            print(f"This month's salary after additional bonus {currentMonthSalary}\n")
            previousMonthSalary = currentMonthSalary 
            
    
        else:
            previousMonthSalary = currentMonthSalary
            
    cumulativeMonthSalary+=currentMonthSalary
    if cumulativeMonthSalary >= 100000:
                Basic_pay += 0.05 * Basic_pay
                       
    
   