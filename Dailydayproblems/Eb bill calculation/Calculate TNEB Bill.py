"""write a program to calculate electricity bill in TamilNadu.
For domestic consumers consuming above 500 units bi-monthly under the 100 unit scheme, 
the consumer has to pay as follows:For first 100 unit it is free,
                                   0-100 units- ₹4.50per unit,
                                   101-400 units- ₹4.50 per unit, 
                                   401-500 units- ₹6.00 per unit, 
                                   501-600 units- ₹8 per unit, 
                                   601-800 units- ₹9 per unit and 
                                   801-1000 units- ₹10 per unit and 
                                   above 1000 units it will be ₹11 per unit."""





units_consumed = float(input("Enter the units consumed: "))
total_bill = 0
   
if units_consumed <= 100:
    # First 100 units are free
    total_bill = 0
elif units_consumed <= 400:
    # 0-100 units: ₹0 per unit
    # 101-400 units: ₹4.50 per unit
    total_bill = 100 * 0 + (units_consumed - 100) * 4.50
elif units_consumed <= 500:
    # 0-100 units: ₹0 per unit
    # 101-400 units: ₹4.50 per unit
    # 401-500 units: ₹6.00 per unit
    total_bill = 100 * 0 + 300 * 4.50 + (units_consumed - 400) * 6.00
elif units_consumed <= 600:
    # 0-100 units: ₹0 per unit
    # 101-400 units: ₹4.50 per unit
    # 401-500 units: ₹6.00 per unit
    # 501-600 units: ₹8.00 per unit
    total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + (units_consumed - 500) * 8.00
elif units_consumed <= 800:
    # 0-100 units: ₹0 per unit
    # 101-400 units: ₹4.50 per unit
    # 401-500 units: ₹6.00 per unit
    # 501-600 units: ₹8.00 per unit
    # 601-800 units: ₹9.00 per unit
    total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + 100 * 8.00 + (units_consumed - 600) * 9.00
elif units_consumed <= 1000:
    # 0-100 units: ₹0 per unit
    # 101-400 units: ₹4.50 per unit
    # 401-500 units: ₹6.00 per unit
    # 501-600 units: ₹8.00 per unit
    # 601-800 units: ₹9.00 per unit
    # 801-1000 units: ₹10.00 per unit
    total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + 100 * 8.00 + 200 * 9.00 + (units_consumed - 800) * 10.00
else:
    # Above 1000 units: ₹11.00 per unit
    total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + 100 * 8.00 + 200 * 9.00 + 200 * 10.00 + (units_consumed - 1000) * 11.00
    
 

print(f"The electricity bill for {units_consumed} units is ₹{total_bill:.2f}")
