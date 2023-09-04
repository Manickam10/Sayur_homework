"""6. Same as the above. Ask the user if they want only the basic or only the advanced or both.
Print what the user is asking. 
Also ask the user what number table they want to print"""

#Initaialize a list to store the list of tables
tables=[]

#Get the user the limit of the list i.e.,how many number tables the user wants
lim=int(input('Enter the limit of the list'))

#For loop to get the input in runtime and store in tables[] list
for i in range(0,lim):
    add=int(input("Enter the tables which you like to print"))
    tables.append(add) #append is a list method which adds the element in the last place of the list

print("1.basic\n2.advanced\n3.Both basic and advanced")
User_input=input("\nEnter what type of table you want to print from above options: ")

if User_input=='1':
    print("My tables")
    print("Easy numbers")
    for j in range(0,len(tables)):
        for i in range(1,11):
          print(f"{tables[j]} * {i} = {tables[j] * i}")
        print("\n")
    print("End of tables")

elif User_input=='2':
    print("My tables")
    print("Advanced numbers")
    for j in range(0,len(tables)):
        for i in range(11,21):
           print(f"{tables[j]} * {i} = {tables[j] * i}")
        print('\n')
    print("End of tables")

elif User_input=='3':
    asteriks='*'*10  #asteriks=**********
    print("My Tables")
    
    print("Easy numbers")
    for j in range(0,len(tables)):
        for i in range(1,11):
          print(f"{tables[j]} * {i} = {tables[j] * i}")
        print('\n')
    
    print("Advanced numbers")
    for j in range(0,len(tables)):
        for i in range(11,21):
           print(f"{tables[j]} * {i} = {tables[j] * i}")
        print('\n')
    print("{}".format(asteriks),"\n")
    print("End of tables")

else:
   print("Invalid input")
