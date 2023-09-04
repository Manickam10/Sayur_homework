"""We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
 for admission in College 1 and College 2."""

#Get the 5 marks from the student
mark1=float(input('Enter mark1 out of 100'))
mark2=float(input('Enter mark2 out 0f 100'))
mark3=float(input('Enter mark3 out of 100'))
mark4=float(input('Enter mark4 out of 100'))
mark5=float(input('Enter mark5 out of 100'))

#Caluclate total marks
if ((mark1>=0 and mark1<=100) and (mark2>=0 and mark2<=100) and (mark3>=0 and mark3<=100) and (mark4>=0 and mark4<=100) and (mark5>=0 and mark5<=100)):
   total_marks=mark1+mark2+mark3+mark4+mark5
   avg_marks=total_marks/5  #Average them by dividing total marks by 5 and then store it in cutoff
   cutoff=avg_marks
   print(f'Your cutoff mark is {cutoff}%' )
else:
    print('please enter valid marks between 0 to 100')


#Different cutoff mark for three colleges fro college admission
College1_cutoff=93
College2_cutoff=89
College3_cutoff=97

#Checking the eligibility 
if cutoff>=College1_cutoff and cutoff>=College2_cutoff and cutoff>=College3_cutoff:
    print("You are eligible for admission in College 1, College 2, and College 3.")
elif cutoff>=College1_cutoff and cutoff>=College2_cutoff:
    print("You are eligible for admission in College 1 and College 2.")
elif cutoff>=College1_cutoff and cutoff>=College3_cutoff:
    print("You are eligible for admission in College 1 and College 3.")
elif cutoff>=College2_cutoff and cutoff>=College3_cutoff:
    print("You are eligible for admission in College 2 and College 3.")
elif cutoff>=College1_cutoff:
    print("You are eligible for admission in College 1.")
elif cutoff>=College2_cutoff:
    print("You are eligible for admission in College 2.")
elif cutoff>=College3_cutoff:
    print("You are eligible for admission in College 3.")
else:
    print("You are not eligible for admission in any of the colleges.")






