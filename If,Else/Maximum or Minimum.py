"""Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or minimum.
Find the answer and print."""
#Function to find the maximum number
def find_max(Number1,Number2,Number3):
    if Number1>Number2:
        if Number1>Number3:
          return Number1
        else:
          return Number3
    elif Number2>Number3:
        return Number2
    else:
        return Number3

#Function to find the minimum number
def find_min(Number1,Number2,Number3):
    if Number1<Number2:
        if Number1<Number3:
          return Number1
        else:
          return Number3
    elif Number2<Number3:
        return Number2
    else:
        return Number3
#Ask the user to enter the three numbers
Number1=int(input('Enter the first number'))
Number2=int(input('Enter the second number'))
Number3=int(input('Enter the third number'))

#Ask the user if they want to find the max of these numbers or minimum.
Choice=input('Enter whether you want to find maximum or minimum among the three numbers ?')
if Choice=="Maximum":
    Maximum_Number=find_max(Number1,Number2,Number3)
    print("The Maximum Number is",Maximum_Number)
elif Choice=="Minimum":
    Minimum_Number=find_min(Number1,Number2,Number3)
    print("The Minimum Number is",Minimum_Number)
else:
    print("Invalid choice")