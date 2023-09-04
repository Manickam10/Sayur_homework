print("1.basic\n2.advanced\n3.Both basic and advanced")
User_input=input("\nEnter what type of table you want to print from above options: ")
table_input=int(input("Enter which number's table you want to print: "))



if User_input=='1':
    print("My tables")
    for i in range(1,11):
        print(f"{table_input} * {i} = {table_input * i}")
    print("End of tables")

elif User_input=='2':
    print("My tables")
    for i in range(11,21):
        print(f"{table_input} * {i} = {table_input * i}")
    print("End of tables")

elif User_input=='3':
    asteriks='*'*10  #asteriks=**********
    print("My Tables")
    
    print("Easy numbers")
    for j in range(1,11):
        print(f"{table_input} * {j} = {table_input * j}")
    
    print("Advanced numbers")
    for j in range(11,21):
        print(f"{table_input} * {j} = {table_input * j}")
    print("{}".format(asteriks),"\n")
    print("End of tables")

else:
   print("Invalid input")






