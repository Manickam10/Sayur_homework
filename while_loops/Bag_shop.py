########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags, whiteBags = 100, 200
totalSales , totalBagsSold = 0,0
redbag_rate,Whitebag_rate=1000,1500
while (totalSales < 10000 or totalBagsSold < 10) :
    #Ask customer for input
    red_bag_purchase=int(input("Enter how many red bags you are going to buy"))
    white_bag_purchase=int(input("Enter how many white bags you are going to buy"))
    if red_bag_purchase <= redBags and white_bag_purchase <= whiteBags:
        #calculate total cost for the bags
        total_cost = (red_bag_purchase * redbag_rate) + (white_bag_purchase * Whitebag_rate)
        totalSales +=  total_cost
        #increment no of bags sold
        totalBagsSold +=  red_bag_purchase + white_bag_purchase
        redBags -= red_bag_purchase
        whiteBags -= white_bag_purchase
    else:
        print("Out of stock")
        continue



print ( f"total sales={totalSales} \ntotal number of bags sold={totalBagsSold}")   