"""Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided. """

number=int(input('Enter any number')) #Prompts the user to enter a number
count=0  #Initializing count=0

if number==0 or number<0:
    print('Enter a valid number')
elif number>0 or number<3:
    print('Enter a number greater than 3')
else:
    while number>=3:# it will keep dividing the number by 3 until the result is less than 3
        number/=3   #number=number/3
        count+=1   #Increments count by 1
        print(f"Result after {count} division(s): {number:.2f}")

#output
print(f"The final result is: {number:.2f} ,Which is less than 3")
print(f"The number was divided {count} times.")
