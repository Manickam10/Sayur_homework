"""Calcualte and print users age - Write a program to ask the user for his/her name and
print 'Hello', user's name.Ask what year they were born.  get the year from the user.
Print 'You are <age> years old'."""

#Function to calculate age
def calculate_age(Birth_year,current_year):
    return current_year-Birth_year

#Get User's name
User_name=input('Enter your name ')
#Get User's Birth Year
Birth_year=int(input('Enter the year you were born '))
current_year=2023
#Calculate the current age of the User
age=calculate_age(Birth_year,current_year)
#Print the result
print('Hello',User_name)
print('You are',age ,'years old')
