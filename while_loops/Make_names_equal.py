"""Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal. 
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cataa, arrow (length is equal by adding a)
"""


def Make_names_equal(name1,name2):
    while len(name1)!=len(name2):  #len means length of the string
        if len(name1)<len(name2):
            name1+='a'   #name1='name1'+'a'
        else:
            name2+='a'   #name2='name2'+'a'
    return name1,name2

#Prompts the user to enter two different names
name1=input('Enter first name ')
name2=input('Enter second name ')
if len(name1)==len(name2):
    print('The two names length are equal ,please enter different names')
else:
    Name1,Name2=Make_names_equal(name1,name2)
    print(Name1)
    print(Name2)
           