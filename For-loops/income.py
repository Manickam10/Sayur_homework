"""Write a program to calculate the income tax in India  for an individual. Input is Salary. Optional input - any deductions.
Up to Rs 3,00,000 -Exempt from tax,
Rs 3,00,000 to Rs 6,00,000-5%,
Rs 6,00,000 to Rs 9,00,000	-10%,
Rs 9,00,000 to Rs 12,00,000-15%,
Rs 12,00,000 to Rs 15,00,000-20% ,
More than Rs Rs 15,00,000-30%    """

# Get the salary and deductions from the user
salary = float(input("Enter your salary: "))
income_slabs=[300000,600000,900000,1200000,1500000]
tax_percentage=[0,0.05,0.1,0.15,0.2,0.3]
tax=0
prev_slab=0
for i in range(len(income_slabs)):
    if salary <= income_slabs[i]:
        tax += (salary - prev_slab) * tax_percentage[i]
        break
    else:
        tax += (income_slabs[i] - prev_slab) * tax_percentage[i]
        prev_slab=income_slabs[i]


print(tax)
