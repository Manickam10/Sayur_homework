"""
In the input, find the first A and last A, print all the letters between  these two A.
If there no A or 2nd A is not found, find the first B and second B and prinyt all the letters between these two B.
If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C.
"""

# Function to find the letters between the two given alphabet.
def FindTheLettersBet(inputString,alpha):
    if (alpha in inputString):
        # fining the index of first alphabet and the last alphabet.
        FirstAlpha = inputString.find(alpha)
        if FirstAlpha >= 0:  
            LastAlpha = inputString.rfind(alpha)
            # if the index of the first alphabet and the last alphabet  are  same then there is only one found.
            if (FirstAlpha == LastAlpha):
                print("There is no A after the first A")
                return False
            else:
                print(f"The Letters between two {alpha} is :{inputString[FirstAlpha+1:LastAlpha]}")
                return True
    else:
        print(f"There is no {alpha} FOund")
        return False


# getting string from the user.
string=input("enter the string:")
letter = input("Which letter's between: ")
if(FindTheLettersBet(string,letter)==False):
    letter = 'b'
    if(FindTheLettersBet(string,letter)==False):
        letter = 'c'
        FindTheLettersBet(string,letter)
        
"""
Expected output:
enter the string:vishnu sivan
Which letter's between: a
There is no A after the first A
There is no b FOund
There is no c FOund
"""