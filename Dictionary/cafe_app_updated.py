import re

menu = {
    "vadai": {"price": 10, "stock": 50, "sales": 0, "profit": 4},
    "tea": {"price": 12, "stock": 45, "sales": 0, "profit": 5},
    "coffee": {"price": 15, "stock": 40, "sales": 0, "profit": 6},
}


for customers in range(1, 11):
    order = input(f"Enter your order [customer {customers}]: ")
    quantity = re.findall(r'\b(\d{2})\b', order)
    items = re.findall(r'\b(vadai|tea|coffee)\b', order.lower())

    for item in items:
        if int(quantity[items.index(item)]) < menu[item]["stock"]:
            menu[item]["stock"] -= int(quantity[items.index(item)])
            menu[item]["sales"] += int(quantity[items.index(item)])
        else:
            print(f"only {menu[item]['stock']} {item} is available:")

print('\n')

# To print sales and profit
for item, info in menu.items():
    final_profit = info["sales"] * info["profit"]
    print(f"Total {item} sold: {info['sales']}\nStock of {item}: {info['stock']}")
    print(f"Profit for {item} is {final_profit}")
    print('\n')
