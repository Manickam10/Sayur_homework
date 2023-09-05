"""Write a program to calculate the income tax in India  for an individual. Input is Salary. Optional input - any deductions.   """

def taxable_income_new(taxable_income):
    tax=0
    # Calculate income tax based on tax slabs
    if 0 < taxable_income <= 250000:
       #Up to Rs 2,50,000 -0%
       tax = 0
       print("You don't need to pay tax")
    elif 250000 < taxable_income <= 500000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       tax = 0.05 * (taxable_income - 250000)
    elif 500000 < taxable_income <= 750000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 7,50,000	-10%
       tax = 0.05 * (500000 - 250000) + 0.1 * (taxable_income - 500000)
    elif 750000 < taxable_income <= 1000000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 7,50,000	-10%
       #Rs 7,50,000 to Rs 10,00,000-15%
       tax = 0.05 * (500000 - 250000) + 0.1 * (750000 - 500000) + 0.15 * (taxable_income - 750000)
    elif 1000000 < taxable_income <= 1250000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 7,50,000	-10%
       #Rs 7,50,000 to Rs 10,00,000-15%
       #Rs 10,00,000 to Rs 12,50,000-20%
       tax = 0.05 * (500000 - 250000) + 0.1 * (750000 - 500000) + 0.15 * (1000000 - 750000) + 0.2 * (taxable_income - 1000000)
    elif 1250000 < taxable_income <= 1500000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 7,50,000	-10%
       #Rs 7,50,000 to Rs 10,00,000-15%
       #Rs 10,00,000 to Rs 12,50,000-20%
       #Rs 12,50,000 to Rs 15,00,000-25%
       tax = 0.05 * (500000 - 250000) + 0.1 * (750000 - 500000) + 0.15 * (1000000 - 750000) + 0.2 * (1250000 - 1000000) + 0.25*(taxable_income-1250000)
    elif taxable_income > 1500000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 7,50,000	-10%
       #Rs 7,50,000 to Rs 10,00,000-15%
       #Rs 10,00,000 to Rs 12,50,000-20%
       #Rs 12,50,000 to Rs 15,00,000-25%
       #Rs 15,00,000 above -30%
       tax = 0.05 * (500000 - 250000) + 0.1 * (750000 - 500000) + 0.15 * (1000000 - 750000) + 0.2 * (1250000 - 1000000) + 0.25*(1500000-1250000) + 0.3*(taxable_income-1500000)
    else:
       print('You have entered wrong input')
    
    return tax

def taxable_income_for_below_60(taxable_income):
    tax=0
    # Calculate income tax based on tax slabs
    if 0 < taxable_income <= 250000:
       #Up to Rs 2,50,000 -0%
       tax = 0
       print("You don't need to pay tax")
    elif 250000 < taxable_income <= 500000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       tax = 0.05 * (taxable_income - 250000)
    elif 500000 < taxable_income <= 1000000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 10,00,000	-20%
       tax = 0.05 * (500000 - 250000) + 0.2 * (taxable_income - 500000)
    elif taxable_income > 1000000:
       #Up to Rs 2,50,000 -0%
       #Rs 2,50,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 10,00,000	-20%
       #Rs 10,00,000 and above-30%
       tax = 0.05 * (500000 - 250000) + 0.2 * (1000000 - 500000) + 0.3 * (taxable_income - 1000000)
    else:
       print('You have entered wrong input')
    
    return tax



def taxable_income_for_age_between_60_and_80(taxable_income):
    tax=0
    # Calculate income tax based on tax slabs
    if 0 < taxable_income <= 300000:
       #Up to Rs 3,00,000 -0%
       tax = 0
       print("You don't need to pay tax")
    elif 300000 < taxable_income <= 500000:
       #Up to Rs 3,00,000 -0%
       #Rs 3,00,000 to Rs 5,00,000-5%
       tax = 0.05 * (taxable_income - 300000)
    elif 500000 < taxable_income <= 1000000:
       #Up to Rs 3,00,000 -0%
       #Rs 3,00,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 10,00,000	-20%
       tax = 0.05 * (500000 - 300000) + 0.2 * (taxable_income - 500000)
    elif taxable_income > 1000000:
       #Up to Rs 3,00,000 -0%
       #Rs 3,00,000 to Rs 5,00,000-5%
       #Rs 5,00,000 to Rs 10,00,000	-20%
       #Rs 10,00,000 and above-30%
       tax = 0.05 * (500000 - 300000) + 0.2 * (1000000 - 500000) + 0.3 * (taxable_income - 1000000)
    else:
       print('You have entered wrong input')
    
    return tax


def taxable_income_for_age_above_80(taxable_income):
    tax=0
    # Calculate income tax based on tax slabs
    if 0 < taxable_income <= 500000:
       #Up to Rs 5,00,000 -0%
       tax = 0
       print("You don't need to pay tax")
    elif 500000 < taxable_income <= 1000000:
       #Up to Rs 5,00,000 -0%
       #Rs 5,00,000 to Rs 10,00,000	-20%
       tax = 0.2 * (taxable_income - 500000)
    elif taxable_income > 1000000:
       #Up to Rs 5,00,000 -0%
       #Rs 5,00,000 to Rs 10,00,000	-20%
       #Rs 10,00,000 and above-30%
       tax = 0.2 * (1000000 - 500000) + 0.3 * (taxable_income - 1000000)
    else:
       print('You have entered wrong input')
    
    return tax



print('1.Old Regime\n2.New Regime')

Regime=(input('Enter which regime you want to calculate your income tax'))

if Regime=='1':
    age=int(input('Enter your age: '))
    # Get the salary and deductions from the user
    salary = float(input("Enter your salary: "))
    deductions = float(input("Enter deductions (if any): "))
    
    if salary >= 0 and deductions >= 0:
       # Calculate taxable income
       taxable_income = salary - deductions
       
       if 0< age <=60:
          tax=taxable_income_for_below_60(taxable_income)
          # Print the calculated tax
          print("Income Tax: Rs", tax)
       
       elif 60< age <=80:
          tax=taxable_income_for_age_between_60_and_80(taxable_income)
          # Print the calculated tax
          print("Income Tax: Rs", tax)
       
       elif age >80:
          tax=taxable_income_for_age_above_80(taxable_income)
          # Print the calculated tax
          print("Income Tax: Rs", tax)
       
       else:
          print('You have entered your age below 0 ')
   
    else:
       print('Please enter a valid salary and deductions')        

elif Regime=='2':
    # Get the salary and deductions from the user
    salary = float(input("Enter your salary: "))
    deductions = float(input("Enter deductions (if any): "))
    
    if salary >= 0 and deductions >= 0:
      # Calculate taxable income
      taxable_income = salary - deductions
      tax=taxable_income_new(taxable_income)
      # Print the calculated tax
      print("Income Tax: Rs", tax)
    
    else:
       print('Please enter a valid salary and deductions')

else:
    print('Enter a valid Regime(say 1 or 2)')





