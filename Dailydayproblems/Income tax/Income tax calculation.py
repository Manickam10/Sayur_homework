"""Write a program to calculate the income tax in India  for an individual. Input is Salary. Optional input - any deductions.
Up to Rs 3,00,000 -Exempt from tax,
Rs 3,00,000 to Rs 6,00,000-5%,
Rs 6,00,000 to Rs 9,00,000	-10%,
Rs 9,00,000 to Rs 12,00,000-15%,
Rs 12,00,000 to Rs 15,00,000-20% ,
More than Rs Rs 15,00,000-30%    """

# Get the salary and deductions from the user
salary = float(input("Enter your salary: "))
deductions = float(input("Enter deductions (if any): "))

# Calculate taxable income
taxable_income = salary - deductions

# Calculate income tax based on tax slabs
if taxable_income <= 300000:
    #Up to Rs 3,00,000 -0%
    tax = 0
    print("You don't need to pay tax")
elif 300000 < taxable_income <= 600000:
    #Up to Rs 3,00,000 -0%
    #Rs 3,00,000 to Rs 6,00,000-5%
    tax = 0.05 * (taxable_income - 300000)
elif 600000 < taxable_income <= 900000:
    #Up to Rs 3,00,000 -0%
    #Rs 3,00,000 to Rs 6,00,000-5%
    #Rs 6,00,000 to Rs 9,00,000	-10%
    tax = 0.05 * (600000 - 300000) + 0.1 * (taxable_income - 600000)
elif 900000 < taxable_income <= 1200000:
    #Up to Rs 3,00,000 -0%
    #Rs 3,00,000 to Rs 6,00,000-5%
    #Rs 6,00,000 to Rs 9,00,000	-10%
    #Rs 9,00,000 to Rs 12,00,000-15%
    tax = 0.05 * (600000 - 300000) + 0.1 * (900000 - 600000) + 0.15 * (taxable_income - 900000)
elif 1200000 < taxable_income <= 1500000:
    #Up to Rs 3,00,000 -0%
    #Rs 3,00,000 to Rs 6,00,000-5%
    #Rs 6,00,000 to Rs 9,00,000	-10%
    #Rs 9,00,000 to Rs 12,00,000-15%
    #Rs 12,00,000 to Rs 15,00,000-20%
    tax = 0.05 * (600000 - 300000) + 0.1 * (900000 - 600000) + 0.15 * (1200000 - 900000) + 0.2 * (taxable_income - 1200000)
else:
    #Up to Rs 3,00,000 -0%
    #Rs 3,00,000 to Rs 6,00,000-5%
    #Rs 6,00,000 to Rs 9,00,000	-10%
    #Rs 9,00,000 to Rs 12,00,000-15%
    #Rs 12,00,000 to Rs 15,00,000-20%
    #More than Rs Rs 15,00,000-30%
    tax = 0.05 * (600000 - 300000) + 0.1 * (900000 - 600000) + 0.15 * (1200000 - 900000) + 0.2 * (1500000 - 1200000) + 0.3 * (taxable_income - 1500000)


# Print the calculated tax
print("Income Tax: Rs", tax)
