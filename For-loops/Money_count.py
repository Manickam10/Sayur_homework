############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.

Sum_money=0
MONEY_COUNT=0
for i in range(5):
    Money=int(input(print("I need some money to go for movie")))
    MONEY_COUNT +=1
    if Money <=10:
        print("Try Again")
        continue
    else:
        if Money>=1000:
            print(f"They gave {Money}\nThank you")
            Sum_money+=Money
            break
        else:
            print(f"They gave {Money}\nThank you")
            Sum_money+=Money

    if Sum_money >=1000:
        break       


print(f"Totally he got{Sum_money}\nTotally he asked {MONEY_COUNT} times to his parents")


    

