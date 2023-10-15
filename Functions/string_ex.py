"""
In the input,find the first A and last A,print all the letters between these two A.
Also print between first B and last B
"""

def printlettersbet(input_string,letter):
    first = input_string.find(letter)
    if first >= 0:
        last = input_string.rfind(letter)
        if last!= first:
            print(f"The Letters between two {letter} is :{input_string[first+1:last]}")
        else:
            print(f"No second {letter}")
    else:
        print(f"No {letter}")

input_string = input("Enter any: ")
letter = input("Which letter's between: ")
printlettersbet(input_string,letter)

"""
Expected output:
Enter any: Brahma vishnu sivan
Which letter's between: a
The Letters between two a is :hma vishnu siv
"""