"""
Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.

"""
# Hard-coded list of student names and their marks in CS
student_names = ["Akash", "Gogul", "Manickam", "Nithis", "Ragul"]
cs_marks = [60, 45, 75, 30, 55]

# Pass mark
pass_mark = 50

# Initialize lists to store passing students and failing students
passing_students = []
failing_students = []

# Iterate through the student names and marks
for i in range(len(student_names)):
    name = student_names[i]
    mark = cs_marks[i]

    # Check if the student passed
    if mark >= pass_mark:
        passing_students.append(f"{name}:{mark}")
    else:
        failing_students.append(name)

# Print the passing students and their marks
print("Passing Students:")
for student in passing_students:
    print(student)

# Print the number of failing students
print("Number of Failed Students:", len(failing_students))
