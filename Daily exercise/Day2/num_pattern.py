"""Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 9)"""


# User_input = int(input("How far to go?  "))
# number = '1'
# output = ''
# nxt=ord(number)
# for num in range(1,User_input+1):
#     output =  output + chr(nxt) + output
#     print(output)
#     nxt=ord(number)+1

rows = int(input("Enter how far to go(upto 9): "))
if 0 < rows <=9:
    for row in range(1, rows+1):
        for col1 in range(row, 0, -1):
            print(col1, end="")
        for col2 in range(2, row+1):
            print(col2, end="")
        print()
else:
    print("Try to enter numbers between 0 to 9")

