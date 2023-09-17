########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

myName = input("Enter your name: ")
# letters = ""
# for letter in myName: 
#     letters += letter
#     print(letters)

for i in range(len(myName)): 
    print(myName[:i+1])


   
   