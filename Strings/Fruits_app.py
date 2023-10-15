"""Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
You can limit the quantity to single digit number."""

#Fruit vendor has a list of fruits
fruits=['apple','orange','banana','grape']
quantity = None
Fruit_asked = None
prev_quantity = None
prev_fruit = None
numbers = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
while True:
    # Ask the customer what they want to buy
    customer_input = input("What do you want to buy?")

    # Check if the customer mentioned a quantity and asked fruit from your list
    words = customer_input.split()
    for word in words:
        if word.isdigit() and len(word) == 1:
            quantity = int(word)
        elif word.lower() in fruits:
            Fruit_asked =  word
        elif word in numbers:
            quantity = numbers.get(word.lower(), 0)

    if quantity == None:
        quantity = int(input("Please Enter the quantity of the fruit u asked: ")) 
    # If a fruit is recognized
    if quantity < 10:
        if Fruit_asked:
            print(f"You want {quantity} {Fruit_asked}.")
        else:
            print("I didn't understand your request. Please specify a fruit and, if needed, a quantity (e.g., 'two apples').")
        if prev_quantity == quantity and prev_fruit == Fruit_asked:
            print("You have already asked for the quantity of the fruit")
        else:
            prev_fruit = Fruit_asked
            prev_quantity = quantity
    # Check if the customer wants to exit the program
    if customer_input.lower() == "exit":
        print("Fruit vendor: Thank you for shopping!")
        break


"""
Expected output:
i want three APPLE
You want 3 APPLE
"""
    





