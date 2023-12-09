"""
Problem 1
In the input, find the first A and last A, print all the letters between these two A.
"""
def printlettersbet(input_string,letter):
    first = input_string.lower().find(letter)
    if first >= 0:
        last = input_string.lower().rfind(letter)
        if last!= first:
            print(f"The Letters between two {letter} is :{input_string[first+1:last]}")
        else:
            print(f"There is No second or last {letter}")
    else:
        print(f"There is No {letter} in the given string")

input_string = input("Enter any passage(strings): ")
letter = 'a'
printlettersbet(input_string,letter)
