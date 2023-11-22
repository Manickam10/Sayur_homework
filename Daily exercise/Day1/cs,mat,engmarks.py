"""
Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
"""
# Hard-coded list of student names and their marks in CS
student_names = ["Akash", "Gogul", "Manickam", "Nithis", "Ragul"]
cs_marks = [90, 95, 75, 30, 55]
Math_marks = [80, 95, 95, 50, 35]
English_marks = [30, 95, 55, 80, 85]
# Pass mark
pass_mark = 50

for i in range(len(student_names)):
    if cs_marks[i]>=pass_mark and Math_marks[i]>=pass_mark and English_marks[i]>=pass_mark:
        if cs_marks[i]>=80 or Math_marks[i]>=80 or English_marks[i]>=80:
            if cs_marks[i]>=90 and Math_marks[i]>=90 and English_marks[i]>=90:
                print(f"{student_names[i]} got A in all subjects")
            elif cs_marks[i]>=90 or Math_marks[i]>=90 or English_marks[i]>=90:
                print(f"{student_names[i]} got atleast one A and the rest B")
