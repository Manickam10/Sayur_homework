"""
Problem 2:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
"""
# Function to find the letters between the two given alphabet.
def PrintTheLettersBet(inputString,alpha):
    if (alpha in inputString):
        # fining the index of first alphabet and the last alphabet.
        FirstAlpha = inputString.find(alpha)
        if FirstAlpha >= 0:  
            LastAlpha = inputString.rfind(alpha)
            # if the index of the first alphabet and the last alphabet  are  same then there is only one found.
            if (FirstAlpha == LastAlpha):
                print(f"There is no {alpha} after the first {alpha}")
                return False
            else:
                print(f"The Letters between two {alpha} is :{inputString[FirstAlpha+1:LastAlpha]}")
                return True
    else:
        print(f"There is no {alpha} FOund in the string")
        return False


# getting string from the user.
string=input("enter the string:")
letter = 'a'
if(PrintTheLettersBet(string,letter)==False):
    letter = 'b'
    if(PrintTheLettersBet(string,letter)==False):
        letter = 'c'
        PrintTheLettersBet(string,letter)
        