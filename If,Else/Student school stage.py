""" Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name 
and print 'Hello', user's name. 
Ask what year they were born.  
eg Hello Chitra, what year were you born?
get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college, based on users age. 
(hint - use if/elif)"""

#Function to find school stage of the user
def get_school_stage(Age):
    if Age < 5:
        return "You are too young for school!"
    elif Age < 6:
        return "You are in Kindergarten."
    elif Age < 12:
        return "You are in Elementary School."
    elif Age < 15:
        return "You are in Middle School."
    elif Age < 19:
        return "You are in High School."
    else:
        return "You are in College or beyond."

#Get user's Name
User_Name=input('Enter the student name ')
#Get user's Birth Year
Birth_year=int(input(f'Hello {User_Name},which year you were born? '))
current_year=2023
#Calculate user's age
Age=current_year-Birth_year
#Passing,age of the user to function and finding out the school stage of the user
School_stage=get_school_stage(Age)
print(School_stage)
