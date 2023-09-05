"""For consumption below 500 units:                            For consumption above 500 units:
    0-100 units: ₹0 per unit                                      Upto 100 unit it is free,
    101-200 units: ₹2.25 per unit                                 101-400 units- ₹4.50 per unit
    201-400 units: ₹4.50 per unit                                 401-500 units- ₹6.00 per unit
    401-500 units: ₹6.00 per unit                                 501-600 units- ₹8 per unit            
                                                                  601-800 units- ₹9 per unit and 
                                                                  801-1000 units- ₹10 per unit and 
                                                                  above 1000 units it will be ₹11 per unit     """


units_consumed = float(input("Enter the units consumed: "))

if units_consumed > 0:
    if units_consumed <= 500:
        total_bill = 0  # First 100 units are free
        # Define arrays for units and rates
        unit_ranges = [100, 200, 400, 500]
        rates = [0, 2.25, 4.50, 6.00]
        i=0

        for i in range(len(unit_ranges)):
            if units_consumed > unit_ranges[i]:
                total_bill += (unit_ranges[i] - unit_ranges[i - 1]) * rates[i]
            else:
                print(unit_ranges[i-1])
                total_bill += (units_consumed - unit_ranges[i - 1]) * rates[i]
                break

        print(f"The electricity bill for {units_consumed} units is ₹{total_bill:.2f}")
    else:
        total_bill = 0  # First 100 units are free
        # Define arrays for units and rates
        unit_ranges = [100, 400, 500, 600, 800, 1000, 10000]
        rates = [0, 4.50, 6.00, 8.00, 9.00, 10.00, 11.00]

        for i in range(len(unit_ranges)):
            if units_consumed > unit_ranges[i]:
                total_bill += (unit_ranges[i] - unit_ranges[i - 1]) * rates[i]
            else:
                total_bill += (units_consumed - unit_ranges[i - 1]) * rates[i]
                break

        print(f"The electricity bill for {units_consumed} units is ₹{total_bill:.2f}")
else:
    print("Please enter valid units consumed")
