"""
Problem 1
Print the following pattern
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

Observe how the nunmbers in the triangle are calculated. 
Do it in two steps. Work on the generating the numbers first in right angle triangle
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

And then work on the final output using proper indendation
"""
#Getting user input
rows = int(input("Enter the no. of rows: "))

#creating a empty list to store previous row values
prev_row = []  

for i in range(rows): #Loop to execute each row one by one
    row = [1]
    if i > 0:
        prev_row_copy = prev_row.copy()#copies the prev_row list to prev_row_copy list
        
        for j in range(len(prev_row_copy) - 1):
            row.append(prev_row_copy[j] + prev_row_copy[j + 1])# To add adjacent values in the prev list and append them in row list
        row.append(1)
    prev_row = row.copy()#copies the row list to prev_row list
    
    #To print the row
    print(' '*(rows-len(row)),end=" ")#To create and print the indentations required for the current row
    for num in row:  #Loop through the row list and print the values in the same row
          print(num, end=" ")
    print()#To create or go to next line



#Pattern without indentations like right angled triangle
#Getting user input
rows = int(input("Enter the no. of rows: "))
prev_row = []

for i in range(rows): #Loop to execute each row one by one
    row = [1]
    if i > 0:
        prev_row_copy = prev_row.copy() #copies the prev_row list to prev_row_copy list
        for j in range(len(prev_row_copy) - 1):
            row.append(prev_row_copy[j] + prev_row_copy[j + 1]) # To add adjacent values in the prev list and append them in row list
        row.append(1)
    prev_row = row.copy() #copies the row list to prev_row list
    
    for num in row: #Loop through the row list and print the values in the same row
        print(num, end=" ")
    print()#To create or go to next line


#ouput
# Enter the no. of rows: 5
#      1 
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# Enter the no. of rows: 5
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1