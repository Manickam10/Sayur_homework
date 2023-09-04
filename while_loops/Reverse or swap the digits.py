"""Write a program that will swap two numbers.if input if 89, output should be 98 (swap the digits)"""

#Function to reverse the number
def reverse_digit(number):
    reversed_number=0
    
    while number > 0:
     digit = number % 10  #Extract the last digit using modulo operation
     reversed_number = reversed_number*10+digit  #
     number //= 10  #Removing the last digit from the number
    return reversed_number


#Get the input number from the user
number = int(input('Enter the number you want to reverse '))
#Passing that number to the function
reversed_number = reverse_digit(number)
#output
print(f'Reversed Number is {reversed_number}')