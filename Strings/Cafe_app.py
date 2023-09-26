import re
menu = ["vadai","tea","coffee"]
price = [10,12,15]
stock = [50,45,40]
sales = [0,0,0]
profit = [4,5,6]
customer_input = []
for customers in range(1,11) :
    order = input(f"Enter your order[customer {customers}]: ")
    quantity = re.findall(r'\b(\d{2}|\d+)\b' , order)
    items = re.findall(r'\b(vadai|tea|coffee)\b',order.lower())
 
    for item in items:
        x = menu.index(item)
        if int(quantity[items.index(item)]) < stock[x] :
            stock[x] -= int(quantity[items.index(item)])
            sales[x] += int(quantity[items.index(item)])
        else :
            print(f"only {stock[x]} {item} is available :" )
        
print('\n')
#To print sales and profit
for index, sale in enumerate (sales) :
    final_profit = sales [index] * profit [index]
    print(f"Total {menu[index]} sold:{sale}\nStock of {menu[index]}:{stock[index]}")
    print(f"profit for {menu[index]} is {final_profit}")
    print('\n')