"""
Program #1
Write a program to check if a given string of parentheses, brackets, and braces is balanced. 
For instance, "({[]})" is balanced, but "({[)})" is not
Input - (Abc[i]) or (Abc[2])
Output true
Input ((Abc[i]) or (Abc[2])) 
Output true
Input ((Abc[i]) or Abc[2)])
Output False
"""

#((Abc[i]) or (Abc[2]))
#(([])([]))

input_string = input("Enter any string: ")
openings = ['(','{','[']
closings = [')','}',']']
stack=[]
for char in input_string:
    if char in openings:
        stack.append(char)
    elif char in closings:
        if stack and stack[-1] == openings[closings.index(char)]:
            stack.pop()

# If the stack is empty, then the string is balanced
if not stack:
    print("Output: True")
else:
    print("Output: False")