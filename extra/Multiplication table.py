"""6. Same as the above. Ask the user if they want only the basic or only the advanced or both.
Print what the user is asking. 
Also ask the user what number table they want to print"""

print("1.basic\n2.advanced\n3.Both basic and advanced")
User_input=input("\nEnter what type of table you want to print from above options: ")
table_input=int(input("Enter which number's table you want to print: "))
#Arrays containing easy numbers and advanced numbers
Easy_numbers=[1,2,3,4,5,6,7,8,9,10]
Advanced_numbers=[11,12,13,14,15,16,17,18,19,20]

if User_input=='1':
    print("My tables")
    for i in range(1,len(Easy_numbers)+1):
        print(f"{table_input} * {Easy_numbers[i-1]} = {table_input * Easy_numbers[i-1]}")
    print("End of tables")

elif User_input=='2':
    print("My tables")
    for i in range(1,len(Advanced_numbers)+1):
        print(f"{table_input} * {Advanced_numbers[i-1]} = {table_input * Advanced_numbers[i-1]}")
    print("End of tables")

elif User_input=='3':
    asteriks='*'*10  #asteriks=**********
    print("My Tables")
    
    print("Easy numbers")
    for j in range(1,len(Easy_numbers)+1):
        print(f"{table_input} * {Easy_numbers[j-1]} = {table_input * Easy_numbers[j-1]}")
    
    print("Advanced numbers")
    for j in range(1,len(Advanced_numbers)+1):
        print(f"{table_input} * {Advanced_numbers[j-1]} = {table_input * Advanced_numbers[j-1]}")
    print("{}".format(asteriks),"\n")
    print("End of tables")

else:
   print("Invalid input")






