def calculate_bill(units):
    total_bill = 0

    if units <= 100:
        total_bill = 0
    elif units <= 400:
        total_bill = 100 * 0 + (units - 100) * 4.50
    elif units <= 500:
        total_bill = 100 * 0 + 300 * 4.50 + (units - 400) * 6.00
    elif units <= 600:
        total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + (units - 500) * 8.00
    elif units <= 800:
        total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + 100 * 8.00 + (units - 600) * 9.00
    elif units <= 1000:
        total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + 100 * 8.00 + 200 * 9.00 + (units - 800) * 10.00
    else:
        total_bill = 100 * 0 + 300 * 4.50 + 100 * 6.00 + 100 * 8.00 + 200 * 9.00 + 200 * 10.00 + (units - 1000) * 11.00
    
    return total_bill

# Example usage
units_consumed = int(input("Enter the units consumed: "))
bill_amount = calculate_bill(units_consumed)
print(f"The electricity bill amount is ₹{bill_amount:.2f}")
