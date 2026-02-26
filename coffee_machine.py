import menu 

 

money = 0 

def report() :
    
    print(f"water: {menu.resources["water"]}ml")
    print(f"milk: {menu.resources["milk"]}ml")
    print(f"coffee: {menu.resources["coffee"]}g")
    print(f"money: {money}")
    

def check_resources(order):
    need_resources = False
    for item in menu.MENU :
        if order == item :
            for ingredient in menu.MENU[item]["ingredients"]:
                if menu.MENU[item]["ingredients"][ingredient] > menu.resources[ingredient]:
                    print(f"you don't have enough {ingredient}")
                    need_resources = True;
    return need_resources         

def process_coins():
   print("enter your money in quarters, dimes, nickels, and pennies: ")

   quarters = int(input("how many quartes?: "))
   dimes = int(input("how many dimes?: "))
   nickles = int(input("how many nickles?: "))
   pennies =  int(input("how many pennies?: "))

   user_money = round((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies),2)
   return user_money


def check_transaction(order, money_received):
    global money
    enough_money  = False
    cost = menu.MENU[order]["cost"]
    if money_received < cost:
        print(f"sorry you don't have enough funds for a {order}. Money refunded")
    elif money_received == cost:
        print("success")
        enough_money = True
        money += cost
    elif money_received > cost:
        change = round(money_received - cost,2)
        enough_money = True
        print (f"here is your change ${change} in dollars")
        money += cost
    return enough_money

def make_cofee(order):
    item  = menu.MENU[order]["ingredients"]

    menu.resources["water"] = menu.resources["water"] - item["water"]
    menu.resources["milk"] = menu.resources["milk"] - item["milk"]
    menu.resources["coffee"] = menu.resources["coffee"] - item["coffee"]
    
    print(f"Here is your {order}, Enjoy!")
 

def use_machine():
    user_input  = input("what would you like? (espresso/capuccino/latte): ").lower()
    if user_input == "report":
        report()
    elif user_input == "off":
        return
    else:
        need_reources = check_resources(order = user_input)
        if need_reources:
            # no need to do anythig here
            1+1
        else:
            user_money = process_coins()
            if check_transaction(order = user_input, money_received = user_money):
                make_cofee(order = user_input)
    use_machine()


use_machine()
