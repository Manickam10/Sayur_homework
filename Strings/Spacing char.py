########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g

inputString = input("Enter any word or string: ")
i = 0 #counter to track the chars
newString = ""
while i < len(inputString):
    newString += inputString[i:i+2]                  #FillinMissingCode (assign the from i, i+1 of inputString)
    newString += " " #add space
    i+=2

print (newString)

#output
"""
Enter any word or string: Sayur learning
Sa yu r  le ar ni ng
"""