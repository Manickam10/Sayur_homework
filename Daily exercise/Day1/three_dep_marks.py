"""
problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students studying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks if all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.

"""

# Function to find the top N marks
def top_3_marks(marks):
    sorted_marks = sorted(marks, reverse=True)[:3]
    return sorted_marks


# Function to calculate average marks with passing mark
def avg_marks_with_passing(marks, passing_mark=50):
    passing_marks=[]
    for mark in marks:
        if mark >= passing_mark:
            passing_marks.append(mark)
    if passing_marks:
        return sum(passing_marks) / len(passing_marks)
    else:
        return 0


# Initialize an empty dictionary to store department information
departments = {}

# Loop through three departments
for i in range(3):
    # Get user input in a single line
    input_user = input(f"Enter department name, number of students, and students' marks for department {i + 1} (comma-separated): ")

    # Split the input into a list using commas as the separator
    input_values = input_user.split(',')

    # Extract values from the list
    department_name = input_values[0].strip()
    num_students = int(input_values[1].strip())
    student_marks=[]
    for mark in input_values[2:]:
        student_mark = int(mark.strip())
        student_marks.append(student_mark)

    # Store department information in the dictionary
    departments[department_name] = {
        'Number of Students': num_students,
        'Student Marks': student_marks
    }


# Initialize variables for combined information
all_student_marks = []

# Loop through departments to perform additional calculations
for department, info in departments.items():
    print(f"\nClass: {department}")

    # Find and print the top 3 marks in each class
    top_marks = top_3_marks(info['Student Marks'])
    print(f"Top 3 Marks: {top_marks}")

    # Find and print the average mark with passing mark in each class
    avg_passing_mark = avg_marks_with_passing(info['Student Marks'])
    print(f"Average Mark with Passing (50): {avg_passing_mark}")

    # Update the list of all student marks for combined calculations
    all_student_marks.extend(info['Student Marks'])

# Find and print the top 3 marks in all classes combined
top_marks_all = top_3_marks(all_student_marks)
print(f"\nTop 3 Marks in All Classes combined: {top_marks_all}")

# Find and print the average mark with passing mark in all classes combined
avg_passing_mark_all = avg_marks_with_passing(all_student_marks)
print(f"Average Mark with Passing (50) in All Classes combined: {avg_passing_mark_all}")

# Find which class has the best average mark and least number of failed students
best_avg_mark = 0
best_class = None
least_num_failed_students = 0
for department, info in departments.items():
    avg_mark = avg_marks_with_passing(info['Student Marks'])
    failed_students=[]
    for mark in info['Student Marks']:
        if mark < 50:
            failed_students.append(mark)
            
        num_failed_students = len(failed_students)


    if avg_mark >= best_avg_mark and num_failed_students <= least_num_failed_students:
        best_avg_mark = avg_mark
        best_class = department
        least_num_failed_students = num_failed_students

print(f"\nClass with the Best Average Mark and Least Number of Failed Students: {best_class}")
