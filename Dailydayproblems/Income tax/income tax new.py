def calculate_tax(taxable_income, slabs, rates):
    tax = 0
    
    for i in range(len(slabs)):
        if taxable_income > slabs[i]:
            tax += (slabs[i] - slabs[i-1]) * rates[i]
        else:
            tax += (taxable_income - slabs[i-1]) * rates[i]
            break

    return tax

def main():
    print('1.Old Regime\n2.New Regime')

    Regime = input('Enter which regime you want to calculate your income tax: ')

    if Regime == '1':
        age = int(input('Enter your age: '))
        salary = float(input("Enter your salary: "))
        deductions = float(input("Enter deductions (if any): "))

        if salary >= 0 and deductions >= 0:
            taxable_income = salary - deductions

            if 0 < age <= 60:
                slabs = [250000, 500000, 1000000]
                rates = [0,0.05, 0.2, 0.3]
                tax = calculate_tax(taxable_income, slabs, rates)
                print("Income Tax: Rs", tax)

            elif 60 < age <= 80:
                slabs = [300000, 500000, 1000000]
                rates = [0,0.05, 0.2, 0.3]
                tax = calculate_tax(taxable_income, slabs, rates)
                print("Income Tax: Rs", tax)

            elif age > 80:
                slabs = [500000, 1000000]
                rates = [0,0.2, 0.3]
                tax = calculate_tax(taxable_income, slabs, rates)
                print("Income Tax: Rs", tax)

            else:
                print('You have entered your age below 0')

        else:
            print('Please enter a valid salary and deductions')

    elif Regime == '2':
        salary = float(input("Enter your salary: "))
        deductions = float(input("Enter deductions (if any): "))

        if salary >= 0 and deductions >= 0:
            taxable_income = salary - deductions
            slabs = [250000, 500000, 750000, 1000000, 1250000, 1500000]
            rates = [0,0.05, 0.1, 0.15,0.2, 0.25, 0.3]
            tax = calculate_tax(taxable_income, slabs, rates)
            print("Income Tax: Rs", tax)

        else:
            print('Please enter a valid salary and deductions')

    else:
        print('Enter a valid Regime (say 1 or 2)')

if __name__ == "__main__":
    main()