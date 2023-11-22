"""
problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function
"""
def are_strings_same(s1, s2):
    # Check if the lengths of both strings are equal
    if len(s1) != len(s2):
        return False
    # Check if str2 is str1 using slice function
    for i in range(len(s1)):
        new_str = s1[i:] + s1[:i]
        if s2 == new_str:
            return True
    
    return False

string1 = input("Enter string1: ")
string2 = input("Enter string2: ")
result = are_strings_same(string1, string2)

if result:
    print(f"{string1} is same as {string2}")
else:
    print(f"{string1} is not same as {string2}")


"""output:
Enter string1: abcd
Enter string2: bcda
abcd is same as bcda

Enter string1: 123456
Enter string2: 234561
123456 is same as 234561
"""

