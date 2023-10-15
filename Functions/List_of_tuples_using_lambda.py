"""
Write a Python program to sort a list of tuples using Lambda.
[("apple", 50),("orange", 15) ,("mango", 30)]
lambda functios - sort by name, sort by cost
"""
# initialized a list of fruits and its cost.
Fruits=[("apple", 50),("orange", 15) ,("mango", 30)]

# sorted function is used and the key is passed with the help of lambda function
SortByName = sorted(Fruits,key=lambda x:x[0]) # here the fruits list is passed as the argument and x[0] refers to fruits[o](name of the fruit)
SortByCost = sorted(Fruits,key=lambda x:x[1]) # here the fruits list is passed as the argument and x[1] refers to fruits[1](cost of the fruit)

print(f"List sorted by name:{SortByName}")
print(f"List sorted by cost:{SortByCost}")


"""Expected output:
List sorted by name:[("apple", 50),("mango", 30),("orange", 15)]
List sorted by cost:[("orange", 15) ,("mango", 30),("apple", 50)]
"""