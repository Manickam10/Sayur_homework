######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

for student in range (1,3):
    #FillinMissingCode  to get studnet name
    for mark in range (1,3):
        inputMark = float (input(f"Enter Mark {mark} for student {student}")) #use formatted string
        print (f"Mark {mark} for student {student} is {inputMark}")