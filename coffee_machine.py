import menu 

 

money = 0 

def report() :
    
    print(f"water: {menu.resources["water"]}ml")
    print(f"milk: {menu.resources["milk"]}ml")
    print(f"coffee: {menu.resources["coffee"]}g")
    print(f"money: {money}")
    

# def check_resources(order):
#     for item in menu.MENU :
#         if order == "espresso":
#             for ingredient in menu.MENU[es]
def check_resources(order):
    need_resources = False
    for item in menu.MENU :
        if order == item :
            # if you are so botthered abouthow the list of needed ingredients 
            # is presented, you can create a list and append the 
            # needed ingredients to it the prinnt the message from it like:
            # you are out of {item 1} and {item 2 }
            for ingredient in menu.MENU[item]["ingredients"]:
                # print(menu.MENU[item]["ingredients"][ingredient])
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

#it needs to know the money that was received and
#the drink that was picked
def check_transaction(order, money_received):
    global money
    enough_money  = False
    cost = menu.MENU[order]["cost"]
    if money_received < cost:
        print(f"sorry you don't have enough funds for a {order}. Money refunded")
    elif money_received == cost:
        print("success")
        enough_money = True
    elif money_received > cost:
        change = round(money_received - cost,2)
        enough_money = True
        print (f"here is your change ${change}")
    money += cost
    return enough_money


def use_machine():
    user_input  = input("what would you like? (espresso/capuccino/latte): ").lower()
    if user_input == "report":
        report()
    elif user_input == "off":
        return
    else:
        check_resources(order = user_input)
        user_money = process_coins()

        if check_transaction(order = user_input, money_received = user_money):
            print("make cofee")
        #see how you can print True or False from need_resources without having to see the print ouput of the function 
        # print(f"need resources = {check_resources(order = user_input)}")
    use_machine()





use_machine()
